function isPalindrome(x: number): boolean {
    let ReversedNumber = 0;
    
   let palindrome;  
    for(let temp = x; temp > 0; temp=Math.floor(temp/10)){
        ReversedNumber = ReversedNumber*10+temp%10;
    }
     console.log(ReversedNumber);
        console.log("regular num:",x);

     if(ReversedNumber === x ){
            palindrome = true;
        }
        else{
            palindrome = false;
        }
    return palindrome;
};
