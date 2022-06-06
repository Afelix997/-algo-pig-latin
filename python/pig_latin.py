import re
def translate(word_or_phrase):
  vowel = list('aeiouAEIOU')
  cons= list('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
  in_list =  re.findall(r"[\w']+|[.,!?;\n]",word_or_phrase )

  for i,word in enumerate(in_list):
    if word[0].isalpha():
      while in_list[i][0] not in vowel:
        in_list[i]=in_list[i][1:] + in_list[i][0]  
      if word[0].lower() +word[1]== 'qu':
        in_list[i]=in_list[i][1:] + in_list[i][0]
      if in_list[i][0] in vowel:
        in_list[i]= in_list[i] + 'ay'
    for letter in word:
      if letter.isupper():
        fix=list(in_list[i].lower())
        fix[0]=fix[0].upper()
        fix = ''.join(fix)
        in_list[i]=fix
                                        
  result=' '.join(in_list)
  return result
       

  

