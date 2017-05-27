#include<iostream>
using namespace std;
class stack
{
    public:
    void push(int *array,int *index,int size,int value)
    {
        if(*index>=size)
            cout<<"Stack Overflow\n";
        else
        {
            *index+=1;
            array[*index]=value;
        }
    }
    void pop(int *array,int *index)
    {
        if(*index<0)
            cout<<"Stack underflow\n";
        else
            *index-=1;
    }
    
};
class queue
{
    public:
    void enqueue(int *array,int *end,int size,int value)
    {
        if(*end>=size)
            cout<<"Queue overflow\n";
        else
        {
            *end+=1;
            array[*end]=value;
        }
    }
    void dequeue(int *array,int *start,int *end)
    {
        if(*end-*start<0)
            cout<<"Queue underflow\n";
        else
            *start+=1;
    }
};