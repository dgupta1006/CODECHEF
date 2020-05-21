#include <bits/stdc++.h>
using namespace std;


int main() {
  int t;
  cin>>t;
  while(t--)
  {
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;++i)
    {
      cin>>a[i];
    }
    int mini=INT_MAX,maxi=1,count=1;
    for(int i=1;i<n;++i)
    {
      if(arr[i]-arr[i-1]<=2)
      {
        count++;
      }
      else
      {
        if(count>maxi)
           maxi=count;
        if(count<mini)
          mini=count;
        count=1;
      }
      if(i==n-1)
      {
        if(count>maxi)
           maxi=count;
        if(count<mini)
          mini=count;
      }
    }
    cout<<"\n";
  }
  return 0;
}
