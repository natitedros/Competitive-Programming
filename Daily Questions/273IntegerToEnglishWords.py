class Solution:
    def numberToWords(self, num: int) -> str:
        power={10**9:"Billion",10**6:"Million",10**3:"Thousand",10**2:"Hundred"}
        digits={90:"Ninety",80:"Eighty",70:"Seventy",60:"Sixty",50:"Fifty",40:"Forty",30:"Thirty", \
        20:"Twenty",19 : "Nineteen",18:"Eighteen",17: "Seventeen",16 : "Sixteen",15:"Fifteen", \
        14:"Fourteen",13:"Thirteen",12:"Twelve",11:"Eleven", 10:"Ten",9:"Nine",8:"Eight",7:"Seven", \
        6:"Six",5:"Five",4:"Four",3:"Three",2:"Two",1:"One"}
        def wordify(num):
            if num==0:
                return ""
            if num >= 100:
                for key,value in power.items():
                    # check if the number is greater than the power keys
                    # if num>key => 100234//100000 => 0 
                    if num//key != 0:
                        # if num is divisible by key, no number to wordify to the right
                        if num%key==0:
                            return wordify(num//key)+" "+value
                        # else, we wordify both the values to the left and right
                        return wordify(num//key)+" "+value+" "+wordify(num%key)
            else:
                # iterate through the digits array and check divisibility by keys
                for key,value in digits.items():
                    if num//key != 0:
                        # if num is divisible by key, no number to wordify to the right
                        if num%key==0:
                            return digits[key]
                        # if a number follows the digit at keyth place of num
                        return digits[key]+" "+wordify(num%key)
        ans = wordify(num)       
        return ans if ans != "" else "Zero"