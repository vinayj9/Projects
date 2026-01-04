import modules.show_menu as show
import modules.add_contacts as add
import modules.view_contacts as view
import modules.search_contact as search
import modules.delete_contact as delete
import modules.load_contacts as load
import modules.save_contacts as save
def main():
    load.load_contacts()
    print('Welcome to your contact book')
    while True:
        print()
        show.show_menu()
        a=input('Select your choice of action(1/2/3/4/5):')
        if a=='1':
            add.add_contacts()
            save.save_contacts()
        elif a=='2':
            view.view_contacts()
        elif a=='3':
            search.search_contact()
        elif a=='4':
            delete.delete_contact()
            save.save_contacts()
        elif a=='5':
            
            print('Goodbye!')
            break
        else:
            print('Invalid input!')
            continue
if __name__ == "__main__":
    main()
