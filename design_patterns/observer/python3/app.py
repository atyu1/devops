import StoryModel
import AdminController
import AdminView
import UserView
import stories

def main():
    # Instantiate a model
    model = StoryModel.StoryModel.get_instance()
    # Insta.. a view
    view_admin = AdminView.AdminView(model)
    view_user = UserView.UserView(model)
    # subscribe view to the model
    model.subscribe(view_admin)
    model.subscribe(view_user)
    #import a story
    view_admin.add_story(stories.class_story)
    # list all stories
    view_admin.list_stories()
    
    print('--------- Add story 2')
    view_admin.add_story(stories.router_story)
    view_admin.list_stories()

    print('-------- User view:')
    view_user.list_stories()

if __name__ == '__main__':
    main()