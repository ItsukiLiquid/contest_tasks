// merey's solution: 06.05.2026, 16:23 KBTU 3 corpus 702.
using System;
using System.Collections.Generic;
using System.Linq;

public class Accumul 
{
	public static string Accum(string s) 
  {
     char[] chars = s.ToCharArray();
     string b = "";
     int count = 0;
     for (int i = 1; i < s.Length + 1; i++)
     {
       for (int j = 1; j < i; j++)
       {
         b += char.ToLower(chars[count]);
       }
       
       b += "-";
       count++;
     }
    
    b = b[0..^1];
    b = char.ToUpper(b[0]) + b.Substring(1);
      
    for (int c = 0; c < b.Length; c++)
    {
      if (b[c] == '-') b = b.Substring(0, c + 1) + char.ToUpper(b[c + 1]) + b.Substring(c + 1);;
    }
    
    b = char.ToUpper(chars[0]) + b;
    
    return b;
  }
}