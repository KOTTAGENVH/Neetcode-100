//YTB Link: https://youtu.be/9UtInBqnCgA?si=8wzO7fadjod3vyfU
const s = "anagram";
const t = "nagaram";
const isAnagram = (s, t) => {
    if (s.length !== t.length) return false;
    
    const count = {};
    
    for (let char of s) {
        count[char] = (count[char] || 0) + 1;
    }
    
    for (let char of t) {
        if (!count[char]) return false;
        count[char]--;
    }
    
    return true;
    }

    //Q3
    