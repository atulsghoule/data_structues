//priority queue
#include<iostream>
#include<climits>
using namespace std;
void max_heapfy(int *array,int index,int size)
{
    int l_ch=2*(index+1)-1,r_ch=2*(index+1),maximum=index;
    if(l_ch<=size && array[l_ch]>array[index])
        maximum=l_ch;
    if(r_ch<=size && array[r_ch]>array[maximum])
        maximum=r_ch;
    if(maximum!=index)
    {
        array[index]=array[maximum]^array[index];
        array[maximum]=array[maximum]^array[index];
        array[index]=array[maximum]^array[index];
        max_heapfy(array,maximum,size);
    }
}
void build_max_heap(int *array,int size)
{
    for(int i=size/2;i>-1;i--)
        max_heapfy(array,i,size);
}
int extract_max(int *array,int size)
{
    if(size<0)
    {
        cout<<"heap under flow";
        return -1;
    }
    int max=array[0];
    array[0]=array[size];
    size-=1;
    max_heapfy(array,0,size);
    return max;
}
void increase_key(int *array,int ind,int key)
{
    if(key<array[ind])
        cout<<"New key is smaller than current key";
    else
    {
        array[ind]=key;
        int parent=((ind+1)/2)-1;
        while(ind>0 &&array[parent]<array[ind])
        {
            array[parent]=array[ind]^array[parent];
            array[ind]=array[ind]^array[parent];
            array[parent]=array[ind]^array[parent];
            ind=parent;
            parent=(parent+1)/2-1;
        }
    }
}
void insert_key(int * array,int size,int key)
{
    size+=1;
    array[size]=INT_MIN;
    increase_key(array,size,key);
}
int main()
{
    int array[15]={1,2,3,4,5,6,7,8,9,10};
    build_max_heap(array,9);
}
