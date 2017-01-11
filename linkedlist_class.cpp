#include<iostream>
using namespace std;
class linked_list
{
    struct node
    {
        int data;
        node *next;
    };
    node *root;
    node *pre;
public:
    linked_list()
    {
        root=NULL;
        pre=NULL;
    }
    void insert_data(int num)
    {
        node *new_node= new node;
        new_node->data=num;
        new_node->next=root;
        root=new_node;
    }
    node* find_data(int num)
    {
        node*search=root;
        if(search->data==num)
        {
            pre=root;
            return search;
        }
        while(search->next!=NULL)
        {
            if((search->next)->data==num)
            {
                pre=search;
                return search->next; 
            }
            search=search->next;
        }
        return NULL;
    }
    bool delete_data(int num)
    {
        node *n=find_data(num);
        if(n==NULL)
            return false;
        else if(n==root)
            root=root->next;
        else
            pre->next=n->next;
        return true;
    }
    void display()
    {
        node* disp=root;
        cout<<"\n";
        while(disp!=NULL)
        {
            cout<<" "<<disp->data;
            disp=disp->next;
        }
        cout<<"\n\n";
    }
    void buff()
    {
        cout<<"-----------------------------------------------\n";
    }
};
int main()
{
    linked_list list;
    int op,num;
    while(true)
    {
        cout<<"\n 1 - Insert\n 2 - Delete\n 3 - Find \n Anyother - Exit\n";
        cout<<"\n Enter option : ";
        cin>>op;
        if(op==1)
        {
            cout<<" Enter a number : ";
            cin>>num;
            list.insert_data(num);
            list.buff();
            cout<<" Data Inserted\n";
            
        }
        else if(op==2)
        {
            cout<<" Enter a number : ";
            cin>>num;
            if(list.delete_data(num)==false)
            {
                list.buff();
                cout<<" Does not exist\n";
            }
            else
            {
                list.buff();
                cout<<" Data deleted\n";
            }
        }
        else if(op==3)
        {
            cout<<" Enter a number : ";
            cin>>num;
            if(list.find_data(num)==NULL)
            {
                list.buff();
                cout<<" Dose not exist\n";
            }
            else
            {
                list.buff();
                cout<<" Exist\n";
            }
        }
        else
            break;
        list.buff();
    }
    list.display();
    return 0;
}