const translate = function (inStr) {
    let vowel = 'aeiou'.split('')
    let cons= 'bcdfghjklmnpqrstvwxyz'.split('')
    let inArr =  inStr.split(/([_\W])/)
    

    

    return inArr
};
console.log(translate("Hi, I'm Zach.\nHow are you?"))