# ==================================================================== 
# ========// Task 1, Subtask 1 - Product Review Analysis //==========
# ==================================================================== 

reviews = [ 
                    "This product is really good. I'm impressed with its quality.", 
                    "The performance of this product is excellent. Highly recommended!",
                    "I had a bad experience with this product. It didn't meet my expectations.", 
                    "Poor quality product. Wouldn't recommend it to anyone.",
                    "The product was average. Nothing extraordinary about it." 
                  ]

key_words = [ "good", "excellent", "bad", "poor", "average"]

modified_reviews = []
for word in key_words:
    for review in reviews:
      if word in review:
          new_text = review.replace(word, word.upper())
          modified_reviews.append(new_text)
      
print(modified_reviews)
   
   
# ==================================================================== 
# ============// Task 1, Subtask 2 - Sentiment Tally //===============
# ====================================================================


reviews = [ 
                    "This product is really good. I'm impressed with its quality.", 
                    "The performance of this product is excellent. Highly recommended!",
                    "I had a bad experience with this product. It didn't meet my expectations.", 
                    "Poor quality product. Wouldn't recommend it to anyone.",
                    "The product was average. Nothing extraordinary about it." 
                  ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Create new list with all lower case letters to compare lowercase words
lower_case_reviews = [x.lower() for x in reviews]

def count_positive_words():
    positive_words_in_reviews = 0
    for word in positive_words:
      for review in lower_case_reviews:
        if word in review:
          print(word)
          positive_words_in_reviews += 1
    
    return f"Number of positive words: {positive_words_in_reviews}"      
    
    
    
def count_negative_words():
    negative_words_in_reviews = 0
    for word in negative_words:
      for review in lower_case_reviews:
        if word in review:
          print(word)
          negative_words_in_reviews += 1
    
    return f"Number of negative words: {negative_words_in_reviews}"  

    
print(count_positive_words())  
print(count_negative_words())  

# ==================================================================== 
# ============// Task 1, Subtask 3 - Review Summary //===============
# ====================================================================

reviews = [ 
                    "This product is really good. I'm impressed with its quality.", 
                    "The performance of this product is excellent. Highly recommended!",
                    "I had a bad experience with this product. It didn't meet my expectations.", 
                    "Poor quality product. Wouldn't recommend it to anyone.",
                    "The product was average. Nothing extraordinary about it. Terrible" 
                  ]
    
    
def review_summary():
  summary_reviews_lst = []
  for review in reviews:
    if(review[30] == " "):
      summary_reviews_lst.append(review[:30:]  + "...")
      
    else:
      closest_space_index = review[:30].rfind(' ')
      summary_reviews_lst.append(review[:closest_space_index:] + "...")
    
  return summary_reviews_lst  
    
print(review_summary())    


# ==================================================================== 
# ============// Task 2, User Input Data Processor //=================
# ====================================================================

while True:
  first_name = input("What is your first name?")
  last_name = input("What is your last name?")
  
  if len(first_name) < 2 or len(last_name) < 2:
    print("First name and last name have to be at least 2 characters")  
  else:
    break


Message = "Your full name is:  {} {}".format(first_name, last_name)
# Removes extra spaces from string  
print(" ".join(Message.split()))