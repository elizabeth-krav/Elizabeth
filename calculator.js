const resultElement = document.getElementById('result')
//console.log(resultElement.textContent)
resultElement.textContent = 42
const num1 = document.getElementById('num1')
const num2 = document.getElementById('num2')
const submitBtn = document.getElementById('submit')
const plusBtn = document.getElementById('plus')
const minusBtn = document.getElementById('minus')
const multiplyBtn = document.getElementById('multiply')
const divideBtn = document.getElementById('divide')
let action = "+"

function printResult(result) {
	if (result < 0) {
			resultElement.style.color = 'red'
	} else {
			resultElement.style.color = 'green'
	}
	resultElement.textContent = result
}

plusBtn.onclick = function() {
	action = '+'
}

minusBtn.onclick = function() {
	action = '-'
}

multiplyBtn.onclick = function() {
	action = '*'
}

divideBtn.onclick = function() {
	action = '/'
}

function counting(inp1, inp2, actionSingn) {
	const num1 = Number(inp1.value)
	const num2 = Number(inp2.value)
	if (actionSingn == '+') {
		return num1 + num2
	} else if (actionSingn == '-') {
		return num1 - num2
	} else if (actionSingn == '*') {
		return num1 * num2
	} else if (actionSingn == '/') {
		return num1 / num2
	}

		
}


submitBtn.onclick = function() {
	const result = counting(num1, num2, action)
	printResult(result)
}

//console.log(typeof sum)