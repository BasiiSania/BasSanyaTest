from django import template


register = template.Library()


@register.tag(name="edit_list")
def do_edit_list(parser, token):
    nodelist = parser.parse(('endedit_list', ))
    try:
        tag_name, obj_name = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    parser.delete_first_token()
    return EditListObjNode(obj_name, nodelist)


class EditListObjNode(template.Node):

    def __init__(self, obj_name, nodelist):
        self.obj_name = obj_name
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        try:
            obj = context[self.obj_name]
        except ValueError:
            msg = '%r object is unnown' % self.obj_name
            raise template.TemplateSyntaxError(msg)
        url = "%r" % str(obj.__class__)
        url = url[1:-2]
        url = url.split(' ')[1]
        url = url[1:-1]
        url = url[(url.find('.')+1):]
        url = url.replace('.models.', '/')
        url = url.replace('contrib.', '')
        url = url.replace('.', '/')
        url = '/admin/' + url + '/%s/' %obj.id
        url = url.lower()
        output = '<a href="'+ url +'">' + output + ' </a>'
        return output
