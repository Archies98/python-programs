#The simplest encryption algorithm! In the ceaser cypher we essentially rotate the characters forward or backward
#the number that is specified. It only encrypts alphabets and preserves the punctuation and numbers.

def ceaser_cypher(string, rotate):
  numeric_codes = [ord(character) for character in string]
  cypher = ''
  for character in string:
    # only encrypt alphabets
    if character.isalpha():
     
     #  for lowercase alphabets 
      if 'a' <= character <= 'z':
        code = ord(character)
        
        # if lower than 'a' then rotate back to 'z'
        if code + rotate < 97:
          cypher_code = 122 - abs((97 - (code + rotate))) + 1
          cypher = cypher + chr(cypher_code)
        
        # if more than 'z' then rotate back to 'a'
        elif code + rotate > 122:
          cypher_code = 97 + abs((122 - (code + rotate))) - 1
          cypher = cypher + chr(cypher_code)
        
        # for non-edge cases
        else:
          cypher_code = code + rotate
          cypher = cypher + chr(cypher_code)
      
      
      # for uppercase letters
      elif 'A' <= character <= 'Z':
        code = ord(character)
        
        # if lower than 'A' then rotate back to 'Z'
        if code + rotate < 65:
          cypher_code = 90 - abs((65 - (code + rotate))) + 1
          cypher = cypher + chr(cypher_code)
        
        # if more than 'Z' then rotate back to 'A'
        elif code + rotate > 90:
          cypher_code = 65 + abs((90 - (code + rotate))) - 1
          cypher = cypher + chr(cypher_code)
        
        # for non-edge cases
        else:
          cypher_code = code + rotate
          cypher = cypher + chr(cypher_code)
    
    
    # for punctuation and spaces
    else:
      cypher = cypher + character
  return cypher

# testing our ceaser cypher implementation 
print(f"'xyz, XYZ' shifted by 4:{ceaser_cypher('xyz, XYZ', 4)}")
print(f"'abc, ABC' shifted by -3: {ceaser_cypher('abc, ABC', -3)}")