import eng_to_ipa as ipa
import numpy as np
from collections import Counter

firstString="what are you working"

secondString="not are you lurking"
thirdString="lube lube goo goo"

candidates=[secondString,thirdString]

def phoneticMatchRating(originalString,candidates):
    #gives a high score to candidates that:
    #match the original string in terms of number of syllables,
    #have repeated phonetics (assonance, alliteration)
    
    #convert originalString and candidate strings into phonetics
    phoneticOriginalString=ipa.convert(originalString)
    candidatePhonetics=[ipa.convert(x) for x in candidates]

    #give a high score if the number of syllables is correct. Max 10
    target=sum(ipa.syllable_count(originalString))
    differences=abs(target - np.array([sum(ipa.syllable_count(x)) for x in candidates]))
    syllableScores=10-differences

    #give a high score if line sounds good as a result of having few unique characters. Between 0 and 10
    #first, strip out "'" and " "
    stripBlanks=[x.replace(" ","") for x in candidatePhonetics]
    stripApostrophes=[y.replace("'","") for y in stripBlanks]
    lengths=np.array([len(x) for x in stripApostrophes])
    uniques=np.array([len(Counter(x)) for x in stripApostrophes])
    assonanceScores=10*(1-uniques/lengths)

    return syllableScores, assonanceScores

def bestChoice(originalString, candidates, syllableWeight, assonanceWeight):
    syllableScores, assonanceScores = phoneticMatchRating(originalString, candidates)
    finalScores = syllableScores * syllableWeight + assonanceScores * assonanceWeight
    print(syllableScores, assonanceScores)
    print(finalScores)
    topScore=max(finalScores)
    for i,words in enumerate(finalScores):
        if words == topScore:
            index = i
            return candidates[i]
    
    
    
print(bestChoice(firstString, candidates, 1, 0.1))
    
    
    

    
