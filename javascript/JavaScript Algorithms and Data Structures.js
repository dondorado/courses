function addUp(num) {
    let total = 0;
    for (i=0; i<=num; i++) {
        total += i;
    }
    return total;
}
function addUp2(num) { 
    return num * (num + 1) / 2
}

function validAnagram(word1, word2) {
    if (word1.length !== word2.length ) {
        return false;
    }

    let obj1 = {};
    let obj2 = {};
    for (let letter of word1) {
        obj1[letter] = ++obj1[letter] || 1
    }
    for (let letter of word2) {
        obj2[letter] = ++obj2[letter] || 1
    }
    for (let letter of word1) {
        if ( !(letter in obj2) || (obj2[letter] !== obj1[letter])) {
            return false
        }
    }
    return true

}

function uniqueValues (arr) {
    let unique = 0
    let i = 0;
    let j = 1;
    while (j <= arr.length) {
        if (arr[i] !== arr[j]) {
            unique += 1;
            i = j;
            j += 1
        } else (
            j += 1
        )

    }
    return unique
}

/***    Frequency Counter    ***/ 

// Write a function called sameFrequency
// Given two positive integers, find out if the two
// numbers have the same frequency of digits.

// Your solution MUST have the following complexities:
// Time: O(N)

//  sameFrequency(182, 281) // true
//  sameFrequency(34, 14) // false
//  sameFrequency(3589578, 5879385) // true
//  sameFrequency(22, 222) // false

function sameFrequency(num1, num2) {

    
    let obj1 = {}
    for (letter of num1.toString()) {
        obj1[letter] = ++obj1[parseInt(letter)] || 1;
    }
    for (letter of num2.toString()) {
        if ( !(letter in obj1) || obj1[letter] === 0) {
            return false;
        } else --obj1[letter]
        

    }
    return true 

}

/*** Coding Exercise 4: Frequency Counter / Multiple Pointers - areThereDuplicates ***/

// Implement a function called, areThereDuplicates which accepts a 
// variable number of arguments, and checks whether there are any
// duplicates among the arguments passed in. You can solve this using 
// the frequency counter pattern OR the multiple pointers pattern.

// areThereDuplicates(1, 2, 3) // false
// areThereDuplicates(1, 2, 2) // true
// areThereDuplicates('a', 'b', 'c', 'a') // true

// Restrictions: 
//     Time - O(N)
//     Space - O(N)
// Bonus:
//     Time - O(N LOG N)  
//     Space - O(1)

function areThereDuplicates(...args) {
    let i = 0;
    while (i < args.length) {
        if (args[i] === args[i + 1]) {
            console.log(i)
            return true
        } else ++i
    }
    return false

}

// Using Frequency Counter Pattern
function areThereDuplicates1(...args) {
    let obj = {};

    for (let val of args) {
        obj[val] = (obj[val] || 0) + 1;
    }
    
    for(let key in obj) {
        if(obj[key] !== 1) return true;
    }
    
    return false;
}


// Using Multiple Pointers Pattern
function areThereDuplicates2(...args) {
    // Two pointers
    args.sort((a,b) => a - b);
    let start = 0;
    let next = 1;

    while(next < args.length) {
        if(args[start] === args[next]) {
            return true;
        }
        start++;
        next++
    }

    return false;
}

// Using Set
function areThereDuplicates3() {
    return new Set(arguments).size !== arguments.length;
}

/*** Multiple Pointers - averagePair ***/ 

// Write a function called averagePair. Given a sorted array of integers and a target average, 
// determine if there is a pair of values in the array where the average of the pair equals the 
// target average. There may be more than one pair that matches the average

// Bonus Contrains:
// Time: O(N)
// Space: O(1)
// Sample Input:
//      averagePair([1,2,3], 2.5); // true
//      averagePair([1,3,3,5,6,7,10,12,19], 8); // true
//      averagePair([-1,0,3,4,5,6], 4.1); // false
//      averagePair([], 4); // false

function averagePair(arr, num) {
    let obj = {};
    for (let element of arr) {
        if (!(element in obj)) {
            obj[element] = 0
        } 
    }
    for (let element of arr) {
        if ( (num * 2 - element) in obj ) {
            return true
        }
    }
    return false
}

/*** Multiple Pointers - isSubsequence ***/ 

// Write a function called isSubsequence which takes in two strings and checks whether 
// the characters in the first string form a subsequence of the characters in the second 
// string. In other words, the function should check whether the characters in the first 
// string appear somewhere in the second string, without their order changing.

// Examples:
// 1     isSubsequence('hello', 'by hecatl in lo world')
// 2     isSubsequence('sing', 'sting')
// 3     isSubsequence('abc', 'abracadabra')
// 4     isSubsequence('abc', 'acb')

// Your solution MUST have AT LEAST the following complexities:
// Time Complexity - O(N + M)
// Space Complexity - O(1)

function isSubsequence(str1, str2) {
    let i = 0;
    while (i < str2.length - 2) {
        if (str2[i] === str1[0]) {
            let j = 1;
            while (str1[j] === str2[i + j]) {
                j++;
                if (j === str1.length) {
                    return true}
        }
            i += j;
            
        } else i++
    }
    return false
}

/*** Sliding Window - maxSubarraySum ***/ 

// Given an array of integers and a number, write a function called maxSubArraySum,
// which finds the maximum sum of a subarray with the length of the number passed
// to the function. Note that a subarray consist of consecutive elements from the 
// original array. In the first example below, [100, 200, 300] is a subarray of the
// original array, but [100,300] is not.

// maxSubarraySum([100,200,300,400], 2) // 700
// maxSubarraySum([1,4,2,10,23,3,1,0,20], 4) // 39
// maxSubarraySum([-3,4,0,-2,6,-1], 2) // 5
// maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1], 2) // 5
// maxSubarraySum([2,3], num) // null

// Constraints:
// Time Complexity - O(N)
// Space Complexity - O(1)

function maxSubarraySum(arr, num) {
    let startTime = performance.now();
    let sum = arr.slice(0, num).reduce((a, b) => a + b);    
    for (let element = 1; element < arr.length - num + 1; element ++ ) {
        let temp = 0;
        temp = arr.slice(element, element + num).reduce((a, b)=> a + b);
        if (temp > sum) sum = temp;
    
    }
    let endTime = performance.now();
    var timeDiff = endTime - startTime;
    
    timeDiff /= 1000;
    // get seconds 
    var seconds = Math.round(timeDiff);
    console.log(seconds + " seconds");
    return sum
}

function maxSubarraySum2(arr, num) {
    let startTime = performance.now();
    let maxSum = 0;
    let tempSum = 0;
    if(num > arr.length) return null;
    
    for (let i = 0; i < num; i++) {
        maxSum += arr[i];
    }
    tempSum = maxSum;
    console.log(tempSum)
    for (let i = num; i < arr.length; i++) {
        tempSum = tempSum - arr[i - num] + arr[i];
        console.log(tempSum)
        maxSum = Math.max(maxSum, tempSum);
    }
    let endTime = performance.now();
    var timeDiff = endTime - startTime;
    timeDiff /= 1000;
    // get seconds 
    var seconds = Math.round(timeDiff);
    console.log(seconds + " seconds");
    
    return maxSum;
}


function compareNumbers(num1, num2) {
    console.log(num1, num2)
    return num2 - num1
}

function bubbleSort(arr) {
    let temp = 0;
    let noSwaps;
    for (let i = arr.length-1 ; i > 0; i--) {
        noSwaps = true;
        for (let j = 0; j < i; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                noSwaps = false;
            }

            
        }
        if (noSwaps) break


    }
    return arr;
}

// console.log(bubbleSort([1, 7, -4, 29, 15, -1034, -200, 37]))

function selectionSort(arr) {
    let temp;
    for (i = 0; i < arr.length; i++) {
        let min = i;
        for (j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[min]) min = j; 
        }
        if (min !== i) {
            temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
    }
    return arr
}

// console.log(selectionSort([1, 7, -4, 29, 15, -1034, -200, 37]))

// function insertionSort(arr) {
//     let temp;
//     for (let i = 1; i < arr.length; i++) {
//         for (let j =i-1; j >= 0; j--) {
//             if (arr[j+1] < arr[j]) {
                
//                 temp = arr[j+1];
//                 arr[j+1] = arr[j];
//                 arr[j] = temp;
                

//             }
//         }
//     }
//     return arr
// }

// bolje resenje
function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        var currentVal = arr[i];
        for (var j =i-1; j >= 0 && arr[j]>currentVal; j--) {
            arr[j+1] = arr[j];
        }
        arr[j+1] = currentVal; // iako se druga for nece izvrsiti, j ce se smanjiti za jos 1, zato ide j + 1     
        }
    return arr    
    }
    


//console.log(insertionSort([1, 7, -4, 29, 15, -1034, -200, 37, 15]))


function merge(arr1, arr2) {
    console.log(`Two arrays that will be merged are: ${arr1} and ${arr2}`)
    let new_array = [];
    let i = 0;
    let j = 0;
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] <= arr2[j]) {
            new_array.push(arr1[i]);
            i++;
        } else {
            new_array.push(arr2[j]);
            j++;
        }
       
    }
    if (i === arr1.length && j !== arr2.length) {
        new_array = new_array.concat(arr2.slice(j, ));
        
    } else if (j === arr2.length && i !== arr1.length) {
        new_array = new_array.concat(arr1.slice(i, ));

        
    }
    console.log(`Array inside merge is: ${new_array}`)
    return new_array

}


// console.log(merge([4], [-3, -1]))

function mergeSort(arr) {
    if (arr.length <= 1) return arr
    else {
        let half = Math.round(arr.length / 2); // ili Math.floor(arr.length / 2)
        console.log(`Array inside mergeSort is: ${arr}`)
        return merge(mergeSort(arr.slice(0, half)), mergeSort(arr.slice(half, )))
         
    }
}

// console.log(mergeSort([3, 7, -4, -15, 19, 25, 16]))

function pivot(arr, start=0, end=arr.length-1) {
    let pivot = arr[start];
    let temp;
    let swapIdex = start;
    for (let i = start + 1; i <= end ; i++ ) {

        if (arr[i] < pivot) {
            swapIdex++;
            temp = arr[swapIdex];
            arr[swapIdex] = arr[i];
            arr[i] = temp;
        }
    }
    temp = arr[swapIdex];
    arr[swapIdex]  = pivot;
    arr[start] = temp;
    return swapIdex;
}
//console.log(pivot([26, 19, 35, 22, 13, 10, 42], 0, 6))
function quickSort(arr, left=0, right=arr.length-1) {
    if (left < right) {
        let pivotIndex = pivot(arr, left, right);
        
        quickSort(arr, left, pivotIndex-1)
        quickSort(arr, pivotIndex + 1, right)
    }
    return arr;
}
// console.log(quickSort([26, 19, 35, 22, 13, -4, -2]))

function getDigit(num, place) {
    // let num_to_string = num.toString();
    // if (num_to_string.length < place) return 0;
    // else return parseInt(num_to_string[num_to_string.length-place]);
    return Math.floor(Math.abs(num) / Math.pow(10, place - 1)) % 10 // bolje resenje
}

//console.log(getDigit(127, 12))

function digitCount(num) {
    // return num.toString().length;
    if (num === 0) return 1;
    return Math.floor(Math.log10(Math.abs(num))) + 1; // bolje resenje
}

//console.log(digitCount(10000))

function maxDigits(arr) {
    let maxDigits = 0;
    for (let i=0; i<arr.length; i++) {
        maxDigits = Math.max(maxDigits, digitCount(arr[i]));
        
    }
    return maxDigits;
}

//console.log(maxDigits([79, 5, 42, 135]))

function radixSort(arr) {
    let max_digits = maxDigits(arr);
    let i = 1;
    while (i <= max_digits) {
        // let temporary_array = [];
        // for (let k = 0; k < 10 ; k++) {
        //     temporary_array.push([]);
        // }
        let temporary_array = Array.from({length: 10}, () => []) // bolje resenje od onog iznad
        for (let j = 0; j < arr.length; j++) {
            let num = arr[j];
            let digit = getDigit(num, i);
            temporary_array[digit].push(num);
        }
        // arr = [];
        // for (let m = 0; m < 10 ; m++) {
        //     arr.push(...temporary_array[m]);
        // }
        arr = [].concat(...temporary_array); // bolje resenje ovog iznad
        i++;
    }
    return arr;
}
//console.log(radixSort([5, 44, 123, 98, 77, 76, 352, 684, -2, 5, 44, 986, 64636, 1388, 546684]))


function makeMaxHeap(arr, index, heapSize) {
    const left = index * 2 + 1;
    const right = index * 2 + 2;

    let largestNum = index;

    if (heapSize > left && arr[largestNum] < arr[left]) {
        largestNum = left;
    }
    if (heapSize > right && arr[largestNum] < arr[right]) {
        largestNum = right;
    }

    if (largestNum !== index) {
        let temp = arr[index];
        arr[index] = arr[largestNum];
        arr[largestNum] = temp;
        makeMaxHeap(arr, largestNum, heapSize);

    }
}

function makeFirstMaxHeap(arr) {
    for (let i = Math.floor(arr.length / 2); i>=0; i--) {
        makeMaxHeap(arr, i, arr.length);
    }
    return arr;
}

function heapSort(arr) {
    // left child = index * 2 + 1
    // right child = index * 2 + 2
    arr = makeFirstMaxHeap(arr);
    let size = arr.length;
    let temp;
    for (let i = arr.length - 1; i > 0; i--) {
        temp = arr[0];
        arr[0]= arr[i];
        arr[i] = temp;
        size--;
        makeMaxHeap(arr, 0, size);
    }
    return arr;
}

//console.log(heapSort([6, 1, -3, 9]))

class Student {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.scores = [];
    }
    addScore(score) {
        this.scores.push(score)
    }
    averageScore() {
        let sum = this.scores.reduce((a, b) => a + b)
        return sum / this.scores.length 
    }
}

// Single Linked List

class NodeSLL {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        if (! this.length) {
            this.head = new NodeSLL(val);
            this.tail = this.head;
        } else {
           let new_node = new NodeSLL(val);
           this.tail.next = new_node;
           this.tail = new_node
        }
        this.length++;
        return this 

    }

    pop() {
        if (!this.length) return undefined;
        else if (this.length === 1) {
            let temp = this.head;
            this.head = null;
            this.tail = null;
            this.length--;
            return temp;
        }
        else {
            let head = this.head;
            let next_head;
            while(head) {
                next_head = head.next;
                if (!next_head.next) {
                    this.tail = head;
                    this.length--;
                    head.next = null;
                    return next_head

                }
                else head = head.next; 
            }
        }
    }

    shift() {
        if (!this.head) return undefined;
        else {
            let temp = this.head;
            this.head = this.head.next;
            this.length--;
            if (this.length===0) this.tail = null;
            return temp
        }
    }

    unshift(val) {
        let new_node = new NodeSLL(val);
        if (!this.head) {
            this.head = new_node;
            this.tail = new_node;            
        } else {
        new_node.next = this.head;
        this.head = new_node;
    }
        this.length++;
        return this
    }

    get(index) {
        if (index < 0 || index >= this.length) return undefined;
        else {
            let counter = this.length - 1;
            let current = this.head;
            for (let i=0; i <= counter; i++) {
                if (i === index) return current
                else current = current.next
            }

        }
    }

    set(index, val) {
        let node = this.get(index);
        if (!node) return false;
        else node.val = val;
        return true;
    }

    insert(index, val) {
        if (index < 0 || index > this.length) return false;
        else if (index === this.length) return !!this.push(val);
        else if (index === 0) return !!this.unshift(val); // !! je not not
        else {
            let previous_node = this.get(index - 1);
            let new_node = new NodeSLL(val);
            new_node.next = previous_node.next;
            previous_node.next = new_node;
            this.length++;
            return true
        }
    }

    remove(index) {
        if (index < 0 || index >= this.length) return undefined;
        else if (index === this.length - 1) return this.pop();
        else if (index === 0) return this.shift();
        else {
            let previous_node = this.get(index - 1);
            let removed_node = previous_node.next;
            previous_node.next = removed_node.next;
            this.length--;
            return removed_node
        }
    }

    reverse() {
        if (this.length === 1) return this;
        let nodes = [];
        let head = this.head;
        nodes.push(head);
        for (let i = 1; i < this.length; i++) {
            head = head.next;
            nodes.push(head); 
        }
        this.head = nodes[nodes.length - 1];
        let current = this.head;
        for (let j = 1; j < nodes.length; j++) {
            current.next = nodes[nodes.length - j - 1];
            current = nodes[nodes.length - j - 1];

        }                                                                                                       
        this.tail = current;
        this.tail.next = null;
        return this;

        

    }


}

// const list = new SinglyLinkedList()

// list.push('Hello')
// list.push('from')
// list.push('Belgrade')

// Double Linked List

class NodeDLL {
    constructor(val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        if (!this.length) {
            this.head = new NodeDLL(val);
            this.tail = this.head;
        } else {
            let node = new NodeDLL(val);
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
        this.length++;
        return this;
    }

    pop() {
        if (!this.length) return undefined;
        else if (this.length === 1) {
            let temp = this.head;
            this.head = null;
            this.tail = null;
            this.length--;
            return temp;
        }
        else {
            let poppped_node = this.tail;
            this.tail = this.tail.prev;
            this.tail.next = null;
            this.length--;
            poppped_node.prev = null;
            return poppped_node;
            
        }
    }

    shift() {
        if (!this.head) return undefined;
        else if(this.length===1) {
            let shiftted_node = this.head;
            this.head = null;
            this.tail= null;
            this.length--;
            return shiftted_node
        }
        else {
            let shiftted_node = this.head;
            this.head = shiftted_node.next;
            this.head.prev = null;
            shiftted_node.next = null;
            this.length--;
            if (this.length===0) this.tail = null;
            return shiftted_node
        }
    }

    unshift(val) {
        if (!this.length) {
            this.head = new NodeDLL(val);
            this.tail = this.head;
        } else {
            let node = new NodeDLL(val);
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        }
        this.length++;
        return this;
    }

    get(index) {
        if (index < 0 || index >= this.length) return undefined;
        let counter = this.length - 1;
        let list_half = Math.floor((this.length - 1) / 2);

        if (index > list_half) {
            let current = this.tail;
            for (let i=counter; i >= list_half; i--) {
                if (i === index) return current
                else current = current.prev
            }
        }
        else {
            let current = this.head;            
            for (let i=0; i <= list_half; i++) {
                if (i === index) return current
                else current = current.next
            }

        }
    }

    set(index, val) {
        let node = this.get(index);
        if (!node) return false;
        else node.val = val;
        return true;
    }

    insert(index, val) {
        if (index < 0 || index > this.length) return false;
        else if (index === this.length) return !!this.push(val);
        else if (index === 0) return !!this.unshift(val); // !! je not not
        else {
            let previous_node = this.get(index - 1);
            let new_node = new NodeSLL(val);
            new_node.next = previous_node.next;
            new_node.prev = previous_node;
            previous_node.next.prev = new_node;
            previous_node.next = new_node;            
            this.length++;
            return true
        }
    }

    remove(index) {
        if (index < 0 || index >= this.length) return undefined;
        else if (index === this.length - 1) return this.pop();
        else if (index === 0) return this.shift();
        else {
            let previous_node = this.get(index - 1);
            let removed_node = previous_node.next;
            previous_node.next = removed_node.next;
            removed_node.next.prev = previous_node;
            removed_node.next = null;
            removed_node.prev = null;
            this.length--;
            return removed_node
        }
    }

    
}

// const list = new DoublyLinkedList();
// list.push(1);
// list.push(11);
// list.push(111);



// Stack

class NodeStack {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        let new_node = new NodeStack(val);
        if (!this.length) {
            this.head = new_node;
            this.tail = new_node;
        } else {
            let previous_head = this.head;
            this.head = new_node;
            new_node.next = previous_head;
        }
        this.length++;
        return this;
    }

    pop() {
        if (!this.length) return undefined;
        let head = this.head;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = head.next;
        }
        this.length--;
        return head;
    }
}

//const stack = new Stack();
//stack.push(8);

// Queue

class NodeQueue {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    enqueue(val) {
        let new_node = new NodeQueue(val);
        if (!this.length) {
            this.head = new_node;
            this.tail = new_node;
        } else {
            this.tail.next = new_node;
            this.tail = new_node;
            // for (let i =1; i < this.length; i++) {
            //     node = node.next;

            // }
            // node.next = new_node;
            // this.tail = new_node;
        }
        this.length++;
        return this;
    }

    dequeue() {
        if (!this.length) return undefined;
        let head = this.head;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = head.next;
        }
        this.length--;
        return head;
    }
}

// const queue = new Queue();
// queue.enqueue(9);

class NodeBST {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right= null;
    }
}

class QueueBFS {
    constructor() {
        this.head = null;
        this.tail = null;
        this.next = null;
        this.length = 0;
    }

    enqueue(node) {
        if (!this.head) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;

        }
        this.length++;
        return this;
    }

    dequeue() {
        let head = this.head;
        this.head = this.head.next;
        head.next = null;
        this.length--;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return head.val;
    }

}

// BST (Binary search tree)

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(val) {
        let new_node = new NodeBST(val);
        if (!this.root) this.root = new_node;
        else {
            let root = this.root;
            while (true) {
                if (root.val > val && root.left === null) {
                    root.left = new_node;
                    break
                }
                else if (root.val > val) {
                    root = root.left;
                }
                else if (root.val < val && root.right === null) {
                    root.right = new_node;
                    break
                }
                else {
                    root = root.right;
                }
            }
        }
        return this;
    }

    find(val) {
        if (!this.root) return false;
        else {
            let root = this.root;
            let found = false;
            while (root && !found) {
                if (root.val > val) {
                    root = root.left;
                }
                else if (root.val < val) {
                    root = root.right;
                }
                else return true;
            }
        }
        return false;
        
    }

    bfs() {
        let queue = new QueueBFS();
        let root = this.root;
        let visited_nodes = [];
        if (!this.root) return 'No root';
        else {            
            queue.enqueue(root);
            while (root) {
                if (root.left) {
                    queue.enqueue(root.left);                   
                }
                if (root.right) {
                    queue.enqueue(root.right)                   
                }
                visited_nodes.push(queue.dequeue());   
                root = queue.head;

            }

        }
        return visited_nodes;
    }

    dfsPreOrder() {
        let visited_nodes = [];
        function traverse(node) {
            visited_nodes.push(node.val);
            if (node.left) traverse(node.left);
            if (node.right) traverse(node.right);
        }
        traverse(this.root);
        return visited_nodes;
            
    }
    
    dfsPostOrder() {
        let visited_nodes = [];
        function traverse(node) {
            if (node.left) traverse(node.left);
            if (node.right) traverse(node.right);
            visited_nodes.push(node.val);
        }
        traverse(this.root);
        return visited_nodes;
            
    }

    dfsInOrder() {
        let visited_nodes = [];
        function traverse(node) {
            if (node.left) traverse(node.left);
            visited_nodes.push(node.val);
            if (node.right) traverse(node.right);
        }
        traverse(this.root);
        return visited_nodes;
            
    }

}

// const bst = new BinarySearchTree();
// bst.insert(65);
// bst.insert(85);
// bst.insert(60);
// bst.insert(71);
// bst.insert(105);
// bst.insert(58);
// bst.insert(62);
// bst.insert(35);
// bst.insert(3);
// bst.insert(104);
// bst.insert(12);






// class BFS {
//     constructor(bst) {
//         this.root = bst.root;
//         this.queue = new QueueBFS();
//         this.visited = [];

//     }

//     search() {
//         if (!this.root) return 'No root';
//         else {
//             let queue = this.queue;
//             let root = this.root;
//             queue.enqueue(root);
//             while (root) {
//                 if (root.left) {
//                     queue.enqueue(root.left);
                   
//                 }
//                 if (root.right) {
//                     queue.enqueue(root.right)
                   
//                 }
//                 this.visited.push(queue.dequeue());   
//                 root = queue.head;

//             }

//         }
//         return this.visited;
//     }
// }

// const bfs = new BFS(bst);



// Max Binary Heap

class MaxBinaryHeap {
    constructor() {
        this.values = [];
    }

    insert(val) {
        this.values.push(val);
        let index = this.values.length - 1;
        let parentIndex = Math.floor((index - 1) / 2);
        while (this.values[index] > this.values[parentIndex]) {
            let temp = this.values[index];
            this.values[index] = this.values[parentIndex];
            this.values[parentIndex] = temp;
            index = parentIndex;
            parentIndex = Math.floor((index - 1) / 2);

        }
        return this;

    }

    extractMax() {
        // const max = this.values[0];
        // const end = this.values.pop();
        // if (this.values.length > 0) {
        //     this.values[0] = end;
        //     let idx = 0;
        //     const length = this.values.length;
        //     const element = this.values[0];
        //     while(true) {
        //         let leftChildIdx = 2 * idx + 1;
        //         let rightChildIdx = 2 * idx + 2;
        //         let leftChild, rightChild;
        //         let swap = null;

        //         if (leftChildIdx < length) {
        //             leftChild = this.values[leftChildIdx];
        //             if(leftChild > element) {
        //                 swap = leftChildIdx;
        //             }
        //         }
        //         if (rightChildIdx < length) {
        //             rightChild = this.values[rightChildIdx];
        //             if (
        //                 (swap === null && rightChild > element) ||
        //                 (swap !== null && rightChild > leftChild)
        //              ) {
        //                 swap = rightChildIdx;
        //             }
        //         }
        //         if (swap === null) break;
        //         this.values[idx] = this.values[swap];
        //         this.values[swap] = element;
        //         idx = swap;



        //     }

        // }
        // return max;
        let lastIdx = this.values.length - 1;
        let root = 0;
        let max = this.values[root];
        let temp = this.values[lastIdx];
        this.values[lastIdx] = this.values[root];
        this.values[root] = temp;
        this.values.pop();
        while(true) {
            let leftChild = root * 2 + 1; // 1
            let rightChild = root * 2 + 2; // 2
            if (leftChild > this.values.length || rightChild > this.values.length) break;
            if (this.values[leftChild] > this.values[root] && 
                (this.values[leftChild] > this.values[rightChild] ||
                !this.values[rightChild] )) {
                temp = this.values[root];
                this.values[root] = this.values[leftChild];
                this.values[leftChild] = temp;
                root = leftChild;
            }
            else if (this.values[rightChild] > this.values[root] && 
                this.values[rightChild] > this.values[leftChild]) {
                temp = this.values[root];
                this.values[root] = this.values[rightChild];
                this.values[rightChild] = temp;
                root = rightChild;
            }
            else break;
        }
        return max;
     }
}

// const heap = new MaxBinaryHeap();
// heap.insert(19);
// heap.insert(22);
// heap.insert(5);
// heap.insert(12);
// heap.insert(3);


class NodePQ {
    constructor(val, priority) {
        this.val = val;
        this.priority = priority;
    }
}

class PriorityQueue {
    constructor() {
        this.values = [];
    }

    enqueue(val, priority) {
        let node = new NodePQ(val, priority);
        this.values.push(node);
        if (this.values.length === 1) return this;
        let parent = Math.floor((this.values.length - 2) / 2);
        let nodeIdx = this.values.length - 1;
        while(true) {
            if(node.priority < this.values[parent].priority) {
                let temp = this.values[parent];
                this.values[parent] = node;
                this.values[nodeIdx] = temp;
                nodeIdx = parent;
                parent = Math.floor((nodeIdx - 1) / 2);
                if (parent < 0) break;
            }
            else break;
        }
        return this;
    }

    dequeue() {
        if (this.values.length === 0) return 'nothing inside PriorityQueue';
        let root = this.values[0];
        if (this.values.length === 2 ) {
            this.values[0] = this.values.pop();
            return root;
        }
        else if (this.values.length === 1 ) {
            this.values = [];
            return root;
        }
        let start = 0;
        this.values[0] = this.values.pop();
        while(true) {
            let leftChildIdx = start * 2 + 1;
            let rightChildIdx = start * 2 + 2;
            let leftChild = this.values[leftChildIdx];
            let rightChild = this.values[rightChildIdx];
            if (!!leftChild) {
                if(!!rightChild) {
                    if (leftChild.priority <= rightChild.priority && leftChild.priority < this.values[start].priority) {
                        let temp = this.values[start];
                        this.values[start] = this.values[leftChildIdx];
                        this.values[leftChildIdx] = temp;
                        start = leftChildIdx;
                    }
                    else if (leftChild.priority > rightChild.priority && rightChild.priority < this.values[start].priority) {
                        let temp = this.values[start];
                        this.values[start] = this.values[rightChildIdx];
                        this.values[rightChildIdx] = temp;
                        start = rightChildIdx;
                    }
                    else break;
                    
                }

                else if (leftChild.priority < this.values[start].priority) {
                    let temp = this.values[start];
                    this.values[start] = this.values[leftChildIdx];
                    this.values[leftChildIdx] = temp;
                    start = leftChildIdx;
                }
                else break;
                
            }
            //console.log(`Start is: ${this.values[start].priority, start}, left child is: ${this.values[leftChildIdx]} and right child is ${this.values[rightChildIdx]}`)
            // if(this.values[start].priority > this.values[leftChildIdx].priority) {
            //     console.log('done')
            // }
            //console.log(this.values[leftChildIdx].priority < this.values[rightChildIdx].priority)
            // if (!!this.values[leftChildIdx] && 
            // (this.values[start].priority > this.values[leftChildIdx].priority) &&
            // ((this.values[leftChildIdx].priority < this.values[rightChildIdx].priority) || !this.values[rightChildIdx])
            // ) {
            //     let temp = this.values[start];
            //     this.values[start] = this.values[leftChildIdx];
            //     this.values[leftChildIdx] = temp;
            //     start = leftChildIdx;
            //     //console.log('if executed')
            // }

            
            // else if (!!this.values[rightChildIdx] && 
            // (this.values[start].priority > this.values[rightChildIdx].priority) &&
            // ((this.values[leftChildIdx].priority > this.values[rightChildIdx].priority) || !this.values[leftChildIdx])
            // ) {
            //     let temp = this.values[start];
            //     this.values[start] = this.values[rightChildIdx];
            //     this.values[rightChildIdx] = temp;
            //     start = rightChildIdx;
            //     //console.log('else if executed')

            // }
            else 
            {
                break};
        }
        return root;


    }
}



// const pq = new PriorityQueue();
// pq.enqueue('extension cord', 3);
// pq.enqueue('charger', 4);
// pq.enqueue('toothpaste', 2);
// pq.enqueue('money', 5);
// pq.enqueue('cellphone', -4);
// pq.enqueue('wallet', 2);
// pq.enqueue('t-short', 7);
// pq.enqueue('trousers', 1);
// pq.enqueue('pants', -7);


// Hash tables

class HashTable{
    constructor(size=53) {
        this.keyMap = new Array(size);
    }
    
    hash(key) {
        let total = 0;
        let weird_prime = 31;
        for (let i = 0; i < Math.min(key.length, 100); i++) {
            let char = key[i];
            let value = char.charCodeAt(0) - 96;        
            total = (total * weird_prime + value) % this.keyMap.length;
            
        }
        return total
    }

    set(key, value) {
        let hashedvalue = this.hash(key);
        if (this.keyMap[hashedvalue] === undefined) {
            this.keyMap[hashedvalue] = [];
        }
        this.keyMap[hashedvalue].push([key, value]);
        
        return this.keyMap;
    }

    

    get(key) {
        let getKeyMapslot = this.hash(key);
        if (this.keyMap[getKeyMapslot] === undefined) return undefined;
        for (let i = 0; i < this.keyMap[getKeyMapslot].length; i++) {
            if (this.keyMap[getKeyMapslot][i][0] === key) {
                return this.keyMap[getKeyMapslot][i];
            }
        }
        return undefined; 

    }

    keys() {

    }
}

// const hashTable = new HashTable(5);
// hashTable.set('pink', 25)
// hashTable.set('blue', 49)


class GraphVertex {
    constructor(vertex) {
        this.vertex = vertex;
        this.next = null;
    }
}

class GraphStack {
    constructor() {
        this.head = null;
        this.length = 0;
    }

    pop() {
        if (this.length === 0) return;
        let head = this.head;
        this.head = this.head.next;
        if (this.length === 1) {
            this.head = null;
            this.next = null;
        }
        this.length--;
        return head.vertex;
    }

    push(vertex) {
        let new_vertex = new GraphVertex(vertex);
        if (this.length === 0) {
            this.head = new_vertex
        } else {
            let head = this.head;
            this.head = new_vertex;
            this.head.next = head;

        }
        this.length++;

    }


}

class GraphQueue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    shift() {
        if (this.length === 0) return;
        let head = this.head;
        this.head = this.head.next;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        }
        this.length--;
        return head.vertex;
    }

    unshift(vertex) {
        let new_vertex = new GraphVertex(vertex);
        if (this.length === 0) {
            this.head = new_vertex;
            this.tail = new_vertex;
        } 
        else if (this.length === 1) {
            this.head.next = new_vertex;
            this.tail = new_vertex;
        }
        else {
            this.tail.next = new_vertex;
            this.tail = new_vertex;

        }
        this.length++;

    }


}


// Graph


class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {
        this.adjacencyList[vertex] = [];
        return this;
    }

    addEdge(v1, v2) {
        this.adjacencyList[v1].push(v2);
        this.adjacencyList[v2].push(v1);
        return this;

    }

    removeVertex(v) {
        for (let i of this.adjacencyList[v]) {
            this.removeEdge(v, i);
        }
        delete this.adjacencyList[v];
        return this;

    }

    removeEdge(v1, v2) {
        // dva nacina
        // this.adjacencyList[v1].splice(this.adjacencyList[v1].indexOf(v2), 1);
        // this.adjacencyList[v2].splice(this.adjacencyList[v2].indexOf(v1), 1);
        this.adjacencyList[v1] = this.adjacencyList[v1].filter(v => v !== v2);
        this.adjacencyList[v2] = this.adjacencyList[v2].filter(v => v !== v1)
        return this;

    }

    dfsRecursion(start) {
        let result = [];
        let list = this.adjacencyList;
        let visited_vertices = {};
        // let dfs = function(node) { I nacin pravljenja funkcije
        //     visited_vertices[node] = true;
        //     result.push(node);
        //     for (let i of list[node]) {
        //         if (result.indexOf(i) === - 1) {
        //             dfs(i);
        //         }
        //     }
        // }
        // dfs(vertex)
        (function dfs(vertex) {
            visited_vertices[vertex] = true;
            result.push(vertex);
            for (let i of list[vertex]) {
                if (result.indexOf(i) === - 1) {
                    dfs(i);
                }
            }
        })(start)

        return result
    }

    dfsIterative(vertex) {
        let s = new GraphStack();
        let result = [];
        let visited_vertices = {};
        let list = this.adjacencyList;
        s.push(vertex);
        while(s.length) {
            vertex = s.pop();
            if ((result.indexOf(vertex) === -1)) {
                result.push(vertex);
                visited_vertices[vertex] = true;
                for (let i of list[vertex]) {
                    if (result.indexOf(i) === -1) s.push(i);
                }
            }
        }
        return result;
        
    }

    bfs(vertex) {
        let q = new GraphQueue();
        let result = [];
        let visited_vertices = {};
        let list = this.adjacencyList;
        q.unshift(vertex);
        while (q.length) {
            vertex = q.shift();
            if ((result.indexOf(vertex) === -1)) {
                result.push(vertex);
                visited_vertices[vertex] = true;
                for (let i of list[vertex]) {
                    if (result.indexOf(i) === -1) q.unshift(i);
                }
            }
        }
        return result;

    }
}

// const graph = new Graph();
// graph.addVertex('Belgrade');
// graph.addVertex('Sibnica');
// graph.addVertex('Nis');
// graph.addVertex('Kursumlija');
// graph.addVertex('Trebinje');
// graph.addVertex('Mostar');
// graph.addVertex('Varna');
// graph.addVertex('Burgas');
// graph.addEdge('Belgrade', 'Sibnica');
// graph.addEdge('Sibnica', 'Nis');
// graph.addEdge('Nis', 'Burgas');
// graph.addEdge('Nis', 'Belgrade');
// graph.addEdge('Varna', 'Burgas');
// graph.addEdge('Varna', 'Belgrade');
// graph.addEdge('Mostar', 'Trebinje');
// graph.addEdge('Sibnica', 'Mostar');
// graph.addEdge('Sibnica', 'Kursumlija');
// graph.addEdge('Nis', 'Kursumlija');
// graph.addEdge('Trebinje', 'Kursumlija');


const graph = new Graph();
graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');
graph.addVertex('D');
graph.addVertex('E');
graph.addVertex('F');
graph.addEdge('A', 'B');
graph.addEdge('A', 'C');
graph.addEdge('B', 'D');
graph.addEdge('C', 'E');
graph.addEdge('D', 'E');
graph.addEdge('D', 'F');
graph.addEdge('E', 'F');
//console.log(graph.dfsRecursion('A'))
//console.log(graph.dfsIterative('A'))
//console.log(graph.bfs('B'))




// Djikstra Algorhitm

class DijkstraPQ {
    constructor() {
        this.values = [];
    }

    enqueue(node) {
        this.values.push(node);
        if (this.values.length === 1) return this;
        let parent = Math.floor((this.values.length - 2) / 2);
        let nodeIdx = this.values.length - 1;
        while(true) {
            if(node.weight < this.values[parent].weight) {
                let temp = this.values[parent];
                this.values[parent] = node;
                this.values[nodeIdx] = temp;
                nodeIdx = parent;
                parent = Math.floor((nodeIdx - 1) / 2);
                if (parent < 0) break;
            }
            else break;
        }
        return this;
    }

    dequeue() {
        if (this.values.length === 0) return 'nothing inside PriorityQueue';
        let root = this.values[0];
        if (this.values.length === 2 ) {
            this.values[0] = this.values.pop();
            return root;
        }
        else if (this.values.length === 1 ) {
            this.values = [];
            return root;
        }
        let start = 0;
        this.values[0] = this.values.pop();
        while(true) {
            let leftChildIdx = start * 2 + 1;
            let rightChildIdx = start * 2 + 2;
            let leftChild = this.values[leftChildIdx];
            let rightChild = this.values[rightChildIdx];
            if (!!leftChild) {
                if(!!rightChild) {
                    if (leftChild.weight <= rightChild.weight && leftChild.weight < this.values[start].weight) {
                        let temp = this.values[start];
                        this.values[start] = this.values[leftChildIdx];
                        this.values[leftChildIdx] = temp;
                        start = leftChildIdx;
                    }
                    else if (leftChild.weight > rightChild.weight && rightChild.weight < this.values[start].weight) {
                        let temp = this.values[start];
                        this.values[start] = this.values[rightChildIdx];
                        this.values[rightChildIdx] = temp;
                        start = rightChildIdx;
                    }
                    else break;
                    
                }

                else if (leftChild.weight < this.values[start].weight) {
                    let temp = this.values[start];
                    this.values[start] = this.values[leftChildIdx];
                    this.values[leftChildIdx] = temp;
                    start = leftChildIdx;
                }
                else break;
                
            }
  
            else 
            {
                break};
        }
        return root;


    }
}

class WeightedGraph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {
        if(!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
    }
    
    addEdge(vertex1, vertex2, weight) {
        this.adjacencyList[vertex1].push({node: vertex2, weight});
        this.adjacencyList[vertex2].push({node: vertex1, weight});
    }

    dijkstra(start, end) {
        
        let pq = new DijkstraPQ();
        let distances = {};
        let visited_nodes = [];
        let trail = {};
        visited_nodes.push(start);
        distances[start] = 0;
        trail[start] = null;
        
        for (let i in this.adjacencyList) {
            if (i !== start) {
                distances[i] = Infinity;
                trail[i] = null;
            }
            

        }

        for (let i = 0; i < this.adjacencyList[start].length; i++) {
            pq.enqueue(this.adjacencyList[start][i]);
            distances[this.adjacencyList[start][i].node] = this.adjacencyList[start][i].weight;
            trail[this.adjacencyList[start][i].node] = start;
            

        }
        //console.log(Object.keys(distances).length)
        //console.log(visited_nodes.includes('A'))
        //console.log(this.adjacencyList[head.node])
        //console.log(visited_nodes);
        while(visited_nodes.length < Object.keys(distances).length) {
            let head = pq.dequeue();
            if(!visited_nodes.includes(head.node)) {
                // pushing unvisited node 
                visited_nodes.push(head.node);
                for (let i = 0; i < this.adjacencyList[head.node].length; i++) {
                    if (!visited_nodes.includes(this.adjacencyList[head.node][i].node)) {
                        // checking if neighbor already exists in visited nodes
                        if(distances[this.adjacencyList[head.node][i].node] > distances[head.node] + this.adjacencyList[head.node][i].weight) { // calculating whether new path is smaller then existing one                            
                            distances[this.adjacencyList[head.node][i].node] = distances[head.node] + this.adjacencyList[head.node][i].weight
                            trail[this.adjacencyList[head.node][i].node] = head.node;
                            pq.enqueue({node: this.adjacencyList[head.node][i].node, weight: distances[this.adjacencyList[head.node][i].node]});
                        }
                    }
                }            
            }
        
            
        }
        let path = '';
        let new_end = end
        while(trail[new_end]) {
            path = '-' + new_end + path;
            new_end = trail[new_end];
        }
        
        return `Shortest distance is ${distances[end]} and path is ${start + path}`


    }
}

// const wg = new WeightedGraph();
// wg.addVertex('A')
// wg.addVertex('B')
// wg.addVertex('C')
// wg.addVertex('D')
// wg.addVertex('E')
// wg.addVertex('F')
// wg.addVertex('G')
// wg.addVertex('H')
// wg.addEdge('A', 'B', 4)
// wg.addEdge('A', 'C', 2)
// wg.addEdge('B', 'E', 4)
// wg.addEdge('B', 'H', 5)
// wg.addEdge('C', 'D', 2)
// wg.addEdge('C', 'F', 4)
// wg.addEdge('D', 'E', 3)
// wg.addEdge('D', 'F', 1)
// wg.addEdge('E', 'F', 1)
// wg.addEdge('E', 'G', 3)
// wg.addEdge('E', 'H', 2)
// wg.addEdge('F', 'G', 6)
// wg.addEdge('G', 'H', 6)


const allConstruct = (target, wordBank, memo={}) => {
    if (target in memo) return memo[target];
    if (target === "") return [[]];

    const result = [];

    for (let word of wordBank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            const suffixWays = allConstruct(suffix, wordBank, memo);
            // console.log(suffixWays, 'before');
            const targetWays = suffixWays.map(way => [word, ...way]);
            // console.log(targetWays, 'target');
            // console.log(suffixWays, 'after');
            result.push(...targetWays);
            // console.log(result, 'result');
            


        }
    }
    memo[target] = result;
    console.log(memo);
    return result;
}

// console.log(allConstruct("purple", ['purp', 'p', 'ur', 'le', 'purple']))
// console.log(allConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))

const gridTraveler = (n, m) => {
    const table = Array(n + 1)
    .fill() // ne ide se u ovo fill, jer ce onda jednu listu da filuje na sve pozicije i kad se menja na nekom indeksu, promenice za sve
    .map(() => Array(m + 1).fill(0)); // zatp se ide sa map, jer callback funkcijom se pravi stalno nova lista
    table[1][1] = 1;

    for (let i = 0; i <= n; i++) {
        for (let j = 0; j <= m; j++) {
            const current = table[i][j];
            if (j + 1 <= m) table[i][j + 1] += current;
            if (i + 1 <= n) table[i + 1][j] += current;

        }
    }
    return table[n][m];

};

// console.log(gridTraveler(1, 1));
// console.log(gridTraveler(2, 3));
// console.log(gridTraveler(3, 2));
// console.log(gridTraveler(3, 3));
// console.log(gridTraveler(18, 18));

const allConstructIterative = (target, wordBank) => {
    const table = Array(target.length + 1)
    .fill()
    .map(() => []);

    table[0] = [[]];

    for (let i = 0; i <= target.length; i++) {
        for (let word of wordBank) {
            if (target.slice(i, i + word.length) === word) {
                const newCombinations = table[i].map(subArray => [...subArray, word]);
                table[i + word.length].push(...newCombinations);
            }
        }
    }

    return table[target.length];
};

// console.log(allConstructIterative rds', ['cat', 'dog']));








