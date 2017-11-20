#include<iostream>
#include<cmath>
using namespace std;
class circluar_queue
{
    public:
    void enqueue(int *array,int *start,int *end,int size,int value)
    {
        if(abs(*start+1-(*end+1))>=size-1)
            cout<<"Queue Overflow\n";
        else
        {
            *end+=1;
            *end%=size;
            array[*end]=value;
        }
    }
    void dqueue(int *array,int *start,int *end,int size)
    {
        if(abs(*start+1-(*end+1))<=0)
            cout<<"Queue Underflow";
        else
        {
            if(*start==0)
                *start=size-1;
            else
                *start-=1;
        }
    }
};
int main()
{
    int array[4]={1,2},size=4;
    int start=0,end=1;
    circluar_queue* ob;
    ob->enqueue(array,&start,&end,size,3);
    ob->enqueue(array,&start,&end,size,4);
    ob->dqueue(array,&start,&end,size);
    ob->enqueue(array,&start,&end,size,6);
    for(int i=0;i<4;i++)
        cout<<array[i]<<" ";
    cout<<endl;
}