# Define the content for the text file
content = """1. **What is the capital of France?**\\n\\t-\\sA)\\sBerlin\\n\\t-\\sB)\\sMadrid\\n\\t-\\sC)\\sParis\\n\\t-\\sD)\\sRome
2. **Which planet is known as the Red Planet?**\\n\\t-\\sA)\\sEarth\\n\\t-\\sB)\\sMars\\n\\t-\\sC)\\sJupiter\\n\\t-\\sD)\\sVenus
3. **Who wrote the play "Romeo and Juliet"?**\\n\\t-\\sA)\\sWilliam\\sShakespeare\\n\\t-\\sB)\\sCharles\\sDickens\\n\\t-\\sC)\\sMark\\sTwain\\n\\t-\\sD)\\sJane\\sAusten
4. **What is the largest ocean on Earth?**\\n\\t-\\sA)\\sAtlantic\\sOcean\\n\\t-\\sB)\\sIndian\\sOcean\\n\\t-\\sC)\\sArctic\\sOcean\\n\\t-\\sD)\\sPacific\\sOcean
5. **Which element has the chemical symbol 'O'?**\\n\\t-\\sA)\\sGold\\n\\t-\\sB)\\sOxygen\\n\\t-\\sC)\\sSilver\\n\\t-\\sD)\\sIron
6. **Who was the first President of the United States?**\\n\\t-\\sA)\\sThomas\\sJefferson\\n\\t-\\sB)\\sAbraham\\sLincoln\\n\\t-\\sC)\\sGeorge\\sWashington\\n\\t-\\sD)\\sJohn\\sAdams
7. **What is the smallest prime number?**\\n\\t-\\sA)\\s1\\n\\t-\\sB)\\s2\\n\\t-\\sC)\\s3\\n\\t-\\sD)\\s5
8. **Which country is known as the Land of the Rising Sun?**\\n\\t-\\sA)\\sChina\\n\\t-\\sB)\\sJapan\\n\\t-\\sC)\\sSouth\\sKorea\\n\\t-\\sD)\\sThailand
9. **What is the main ingredient in guacamole?**\\n\\t-\\sA)\\sTomato\\n\\t-\\sB)\\sAvocado\\n\\t-\\sC)\\sOnion\\n\\t-\\sD)\\sPepper
10. **Which is the longest river in the world?**\\n\\t-\\sA)\\sAmazon\\sRiver\\n\\t-\\sB)\\sNile\\sRiver\\n\\t-\\sC)\\sYangtze\\sRiver\\n\\t-\\sD)\\sMississippi\\sRiver"""

# Write the content to a text file
with open("mcq_questions.txt", "w") as file:
    file.write(content)

print("The file 'mcq_questions.txt' has been created with the provided multiple-choice questions and answers.")