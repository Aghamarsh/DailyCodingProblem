#include<bits/stdc++.h>
using namespace std;
 
typedef long long ll;
 
 
int main()
{
    ll t;
    cin>>t;
 
    // The original given array of numbers   
    ll a[t];
    
    //Hash Table
    ll ar[105];
//Based on the maximum integer of the array.. select appropriate hash function
    ll hash = 101;
    
    for(ll i=0;i<105;i++)
    ar[i]=0;
    
    ll temp;
    
    for(ll i=0;i<t;i++)
    {
        //insert values into the hash table
        cin>>a[i];
        temp=a[i];
        ll key = temp%hash;
        ar[key]=1;
    }

    ll sum;
    cin>>sum;
    
    int flag = 0;
    
    for(int j=0;j<t;j++)
    {
        temp = sum - a[j];
        
    // search for the other element in the array        
        
        if(ar[temp]==1)
        {
            flag=1;
            cout<<"True"<<endl;
            break;
        }
    }
    
    if(flag==0)
    cout<<"False"<<endl;
}  
