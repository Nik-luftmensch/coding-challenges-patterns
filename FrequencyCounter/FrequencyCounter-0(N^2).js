let list1 = [1,2,3,2]
let list2 = [9,1,4,4]

function same (list1,list2){
    if (list1.length != list2.length){
        return false
    }
    for (let i=0; i==list1.length; i++){
        let correctIndex = list2.indexOf(list1[i]**2)
        if (correctIndex === -1){
            return false
        }
        list2.splice(correctIndex,1)
    }
    return true
}