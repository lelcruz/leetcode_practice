function twoSum(nums: number[], target: number): number[] {

    for(let i = 0; i < nums.length; i++){
        for(let j=1+i; j <nums.length; j++){
             const sum = nums[i]+nums[j];
            if(target == sum)
            {
                
               return [i,j];
            }
            
        } 
        
    }
    
};
