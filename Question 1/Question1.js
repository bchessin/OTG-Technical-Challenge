//Very similar to the Hamming weight problem
function getNumberofOnes(n, count) {
    if (n > 0) {
      var newN = n & (n-1);
      var newCount = count + 1;
      return getNumberofOnes(newN, newCount)
    }
    return count;
}
console.log(getNumberofOnes(15, 0));