#
# textmodel.py
#
# TextModel project!
#
# Name(s): Irene Tang and Patrick Liu
#
import string
import math
from porter import create_stem
import numpy as np
from astropy.table import Table, Column



class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        # 
        # The text in the model, all in a single string--the original
        # and "cleaned" versions.
        #
        self.text = ''            # No text present yet
        self.cleanedtext = ''     # Nor any cleaned text yet
                                  # ..(cleaned == only letters, all lowercase)

        #
        # Create dictionaries for each characteristic
        #
        self.words = {}           # For counting words
        self.wordlengths = {}     # For counting word lengths
        self.stems = {}           # For counting stems
        self.sentencelengths = {} # For counting sentence lengths
        
        # Create another dictionary of your own
        #
        self.myparameter = {}     # For counting ___________

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = f'Words:\n{str(self.words)}\n\n'
        s += f'Word lengths:\n{str(self.wordlengths)}\n\n'
        s += f'Stems:\n{str(self.stems)}\n\n'
        s += f'Sentence lengths:\n{str(self.sentencelengths)}\n\n'
        s += f'MY PARAMETER:\n{str(self.myparameter)}\n\n'
        s += '+'*55 + '\n'
        s += f'Text[:42]    {self.text[:42]}\n'
        s += f'Cleaned[:42] {self.cleanedtext[:42]}\n'
        s += '+'*55 + '\n\n'
        return s

    # We provide two text-adding methods (functions) here:
    def addRawText(self, text):
        """addRawText accepts self (the object itself)
                      and text, a string of raw text to add.
           Nothing is returned from this method, but
           the text _is_ added.
        """
        self.text += text 
        self.cleanedtext += self.cleanString(self.text) 

    # The second one adds text from a file:
    def addFileText(self, filename):
        """addFileText accepts a filename.
            
           Nothing is returned from this method, but
           the file is opened and its text _is_ added.

           If the file is not present, it will crash!
        """
        f = open(filename, 'r', encoding='latin1')
                               # The above may need utf-8 or utf-16, depending
        text = f.read()        # Read all of the contents into text 
        f.close()              # Close the file
        self.addRawText(text)  # Uses the previous method!

    # Include other functions here.
    # In particular, you'll need functions that add to the model.

    def makeSentenceLengths(self):
        """Creates the dictionary of sentence lengths
               should use self.text, because it needs the punctuation!
        """
        LoW = self.text.split()
        counter = 0
        self.sentencelengths = {}

        for word in LoW:
            if word[-1] != '.' and word[-1] != '!' and word[-1] != '?':
                counter += 1
            else:
                counter += 1
                if counter in self.sentencelengths:
                    self.sentencelengths[counter] += 1
                else: 
                    self.sentencelengths[counter] = 1 
                # self.sentencelengths[counter] = self.sentencelengths.get(counter,0)+1
                counter = 0
                
                # Not implemented yet (pass is the empty statement)
                # See description


    def cleanString(self, s):
        """Returns the string s, but
           with only ASCII characters, only lowercase, and no punctuation.
           See the description and hints in the problem!
        """

        s = s.encode("ascii", "ignore")   # Ignores non-ASCII characters
        s = s.decode()         # Decodes it back to a string (with the non-ACSII characters removed)
        for p in string.punctuation:
            s = s.replace(p,'')                      # ..things for now  
        result = s.lower()    # Not implemented fully: this just lower-cases
        return result
    
    def makeWordLengths(self):
        """This method is similar to makeSentenceLengths—except that it makes a 
           dictionary of the word-length features
        """

        cleanString = self.cleanString(self.text)
        self.wordlengths = {}
        LoW = cleanString.split()

        for i in range(len(LoW)):
            if len(LoW[i]) in self.wordlengths:
                self.wordlengths[len(LoW[i])] +=1
            else:
                self.wordlengths[len(LoW[i])] = 1
        return  

    def makeWords(self):
        """similar to makeWordLengths except it makes a dictionary of cleanedwords"""
        cleanString = self.cleanString(self.text)
        self.words = {}
        LoW = cleanString.split()

        for i in range(len(LoW)):
            if LoW[i] in self.words:
                self.words[LoW[i]] += 1
            else: self.words[LoW[i]] = 1
        
        return 
    
    def makeStems(self):
        """except that it makes a dictionary of the stems of the wordsthemselves (cleaned!)"""
        cleanString = self.cleanString(self.text)
        self.stems = {}
        LoW = cleanString.split()
        
        for i in range(len(LoW)):
            if create_stem(LoW[i]) in self.stems:
                self.stems[create_stem(LoW[i])] += 1
            elif create_stem(LoW[i]) not in self.stems:
                self.stems[LoW[i]] = 1
        return 
    
    def smallestValue(self, nd1, nd2):
        """smallestValue accepts any two model dictionaries nd1and nd2 and returns the 
           smallest positive value acrossthe two.
        """
        v1 = nd1.values()
        v2 = nd2.values()
        if min(v1) < min(v2):   return min(v1)
        elif min(v1) > min(v2): return min(v1)

    
    def normalizeDictionary(self, d):
        """normalizeDictionary should accept any single one ofthe model dictionaries d and
           return a normalizedversion.
        """
        norm_dict = {}
        v = d.values()

        for i in d:
            norm_dict[i] = d[i] / sum(v)
        return norm_dict

    def makePunctuation(self):
        """makePunctuation uses the text in self.text to createthe punctuation dictionary.
        """
        self.punctuation = {}
        c = 0
        ListoS = list(self.text)

        for i in ListoS:
            if i == '.':
                if '.' in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1
            if i == '!':
                if '!' in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1
            if i == ',':
                if ',' in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1
            if i == '?':
                if '?' in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1
            if i == ':':
                if ':' in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1
            if i == ';':
                if ';' in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1
            if i == '"':
                if '"' in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1
            if i == "'":
                if "'" in self.punctuation: self.punctuation[i] += 1
                else:   self.punctuation[i] = 1

    def compareDictionaries(self, d, nd1, nd2):
        """compareDictionaries computes the log-probability thatthe dictionary d arose 
           from the distribution of datain the normalized dictionary nd1 and that in 
           normalizeddictionary nd2.
        """
        total_log_prob = 0.0
        total_log_prob_2 = 0.0
        epsilon = self.smallestValue(nd1, nd2) / 2

        for k in d:
            if k in nd1:    total_log_prob += d[k] * math.log(nd1[k])
            else:   total_log_prob += d[k] * math.log(epsilon)
        for k in d:
            if k in nd2:    total_log_prob_2 += d[k] * math.log(nd2[k])
            else:   total_log_prob_2 += d[k] * math.log(epsilon)
        comp = [total_log_prob, total_log_prob_2]

        return comp
    
    def createAllDictionaries(self):
        """Through this function, we can create out all five of self's dictionaries in full"""
        self.makeSentenceLengths()
        self.makeWords()
        self.makeStems()
        self.makePunctuation()
        self.makeWordLengths()

    def compareTextWithTwoModels(self, model1, model2):
        """compareTextWithTwoModels runs the compareDictionariesmethod for each of the 
           feature dictionaries in newmodelagainst the corresponding normalized 
           dictionaries inmodel1 and model2.
        """
        words = self.compareDictionaries(self.words, model1.normalizeDictionary(model1.words), model2.normalizeDictionary(model2.words))
        wordlengths = self.compareDictionaries(self.wordlengths,model1.normalizeDictionary(model1.wordlengths),model2.normalizeDictionary(model2.wordlengths))
        sentencelengths = self.compareDictionaries(self.sentencelengths,model1.normalizeDictionary(model1.sentencelengths), model2.normalizeDictionary(model2.sentencelengths))
        stems = self.compareDictionaries(self.stems, model1.normalizeDictionary(model1.stems), model2.normalizeDictionary(model2.stems))
        punctuation = self.compareDictionaries(self.punctuation, model1.normalizeDictionary(model1.punctuation), model2.normalizeDictionary(model2.punctuation))

        w_1 = ("%0.2f" % words[0])
        wl_1 = ("%0.2f" % wordlengths[0])
        sl_1 = ("%0.2f" % sentencelengths[0])
        st_1 = ("%0.2f" % stems[0])
        pct_1 = ("%0.2f" % punctuation[0])
        w_2 = ("%0.2f" % words[1])
        wl_2 = ("%0.2f" % wordlengths[1])
        sl_2 = ("%0.2f" % sentencelengths[1])
        st_2 = ("%0.2f" % stems[1])
        pct_2 = ("%0.2f" % punctuation[1])

        print("Overall Comparison:")
        print()

        name = np.array(["words", "wordlengths", "sentencelengths", "stems","punctuation"])
        TM1 = [w_1, wl_1, sl_1, st_1, pct_1]
        TM2 = [w_2, wl_2, sl_2, st_2, pct_2]

        t = Table([name, TM1, TM2], names = ("name", "vsTM1", "vsTM2"))
        
        print(t)
        print()

        # For counting number of features won by each model
        pt1 = 0
        pt2 = 0
        weight_1 = 0
        weight_2 = 0

        if words[0] > words[1]: 
            pt1 += 1  
            weight_1 += 0.35
        else: 
            pt2 += 1  
            weight_2 = 0.35
        
        if wordlengths[0] > wordlengths[1]:
            pt1 += 1
            weight_1 += 0.15
        else:
            pt2 += 1
            weight_2 += 0.15
        
        if sentencelengths[0] > sentencelengths[1]:
            pt1 += 1
            weight_1 += 0.15
        else:
            pt2 += 1
            weight_2 += 0.15
        
        if stems[0] > stems[1]:
            pt1 += 1
            weight_1 += 0.20
        else:
            pt2 += 1
            weight_2 += 0.15
        
        if punctuation[0] > punctuation[1]:
            pt1 += 1
            weight_1 += 0.15
        else:
            pt2 += 1
            weight_2 += 0.15
        print()

        print("=== Model 1 has higher probabilities on ", pt1 , " features.")
        print("=== Model 2 has higher probabilities on ", pt2, " features." )

        print()
        if weight_1 > weight_2: print("=== Model 1 is the better match! ===")
        elif weight_1 == weight_2: print("=== Emmm, I don't know ===")
        else: print("=== Model 2 is the better match! ===")
# And let's test things out here...
print(" +++++++++++ Model 1 +++++++++++ ")
TM1 = TextModel()
TM1.addFileText("train1.txt")
TM1.createAllDictionaries() # provided in hw description
print(TM1)

print(" +++++++++++ Model 2 +++++++++++ ")
TM2 = TextModel()
TM2.addFileText("train2.txt")
TM2.createAllDictionaries() # provided in hw description
print(TM2)

print(" +++++++++++ Test Text 1 +++++++++++ ")
TM_T1 = TextModel()
TM_T1.addFileText("test1.txt")
TM_T1.createAllDictionaries() # provided in hw description
print(TM_T1)
print()

print(" +++++++++++ Test Text 2 +++++++++++ ")
TM_T2 = TextModel()
TM_T2.addFileText("test2.txt")
TM_T2.createAllDictionaries() # provided in hw description
print(TM_T2)
print()

TM_T1.compareTextWithTwoModels(TM1, TM2)
print()
TM_T2.compareTextWithTwoModels(TM1, TM2)
