count = 0
while count < 30:
    eLow,eMedium,eHigh = checkEmotion(emotion[count])
    pLow,pMedium,pHigh = checkProvoke(provoke[count])
    Ya,Tidak = inference(eLow,eMedium,eHigh,pLow,pMedium,pHigh)
    hasil = defuzzification(Ya,Tidak)
    if hasil < 55.0:
        hoax = "No"
    elif hasil >= 55.0:
        hoax = "Yes"
print("News : ",news[count]," Emotion : ",emotion[count]," Provoke : ",provoke[count]," Hoax : ", hoax)
count += 1