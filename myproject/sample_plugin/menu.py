# Create a few extra custom menus here

from menus.base import NavigationNode  # , Menu
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from menus.base import Modifier


"""
    If you extend Menu, it will by default come under level 0 of the
    main menu or if parent id is specified then that menu item will come
    under the specified parent.

    Alternatively you may choose to extend from CMSAttachMenu.
    In this case the menu appears under Attached Menu option under
    Page Settings -> Advanced Settings with the 'name' as specified.
    You may choose to integrate this menu with which ever page/s you want.
"""


class TestMenu(CMSAttachMenu):  # or (Menu)

    name = _('ExtraMenu')  # Name of the menu

    # This method is used to create the Menu
    def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_('sample root page'), "/", 1)
        n2 = NavigationNode(_('sample settings page'), "/bye/", 2)
        n3 = NavigationNode(_('sample account page'), "/hello/", 3)
        n4 = NavigationNode(_('sample my profile page'), "/hello/world/", 4, 3)
        """
            NavigationNode (To create a menu item):
                1st Arg : Name to appear in the menu
                2nd Arg : Url to load when the menu item is clicked
                3rd Arg : ID of the menu item
                4th Arg : If in case this item is a child of another
                            menu item, then the id of the parent item.
        """

        nodes.append(n1)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(TestMenu)


class MyMode(Modifier):
    """

    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        count = 0
        for node in nodes:
            node.counter = count
            count += 1
        return nodes

menu_pool.register_modifier(MyMode)


class Level(Modifier):
    """
    marks all node levels
    """
    post_cut = True

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if breadcrumb:
            return nodes
        for node in nodes:
            if not node.parent:
                if post_cut:
                    node.menu_level = 0
                else:
                    node.level = 0
                self.mark_levels(node, post_cut)
        return nodes

    def mark_levels(self, node, post_cut):
        for child in node.children:
            if post_cut:
                child.menu_level = node.menu_level + 1
            else:
                child.level = node.level + 1
            self.mark_levels(child, post_cut)

menu_pool.register_modifier(Level)
