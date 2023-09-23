var selected_task;
var selected = false;
var selected_answer;
var last_selected_task_id;
var colors = ['yellow', 'red', 'blue', 'green', 'gray', 'greenyellow', 'cyan']
var color_id = 0
var last_page_id = 0;
function openTask(evt, cityName) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	document.getElementById(cityName).style.display = "block";
	evt.currentTarget.className += " active";

	var true_q = qestion.length - qestion.reduce((a, b) => a + b, 0)
	document.getElementById("all_answer").innerHTML = 'Барлығы ' + all_questions
	document.getElementById("true_answer").innerHTML = 'Дұрыс ' + true_q
	document.getElementById("false_answer").innerHTML = 'Қате ' + qestion.reduce((a, b) => a + b, 0)
	document.getElementById("id_all_task").value = all_questions
	document.getElementById("id_true_task").value = true_q
	document.getElementById("id_false_task").value = qestion.reduce((a, b) => a + b, 0)
	var fasle_question = localStorage.getItem('flase_question_body');
	document.getElementById("id_user_false_answers").value = fasle_question
	console.log(fasle_question)
}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

function checkAnswer(task, user, result, input_block, input_style, task_status, question_body) {  
	var user_answer = document.getElementById(user).value;	
	var true_answer = localStorage.getItem(task);
	if (user_answer == true_answer) {
		console.log(true)
		document.getElementById(result).innerHTML = 'Дұрыс'; 
		$("#" + input_style).css("background", '#02a0da');
		qestion.push(0)
		localStorage.setItem(task_status, 'true')


	} else {
		console.log(false)
		document.getElementById(result).innerHTML = 'Қате'; 
		$("#" + input_style).css("background", 'red');
		qestion.push(1) 
		localStorage.setItem( task_status, 'false' )
		fasle_questions_in_answer += question_body;
		localStorage.setItem( 'flase_question_body', fasle_questions_in_answer );

	}
	$("#" + input_block).css("display", 'none');
}

function checkAnswerTest(user_answer, true_answer, result, input_style, task_test_block, task_status, question_body) {
	if (user_answer == true_answer) {
		console.log(true)
		document.getElementById(result).innerHTML = 'Дұрыс'; 
		$("#" + input_style).css("background", '#02a0da');
		qestion.push(0)
		localStorage.setItem(task_status, 'true')

	} else {
		console.log(false)
		document.getElementById(result).innerHTML = 'Қате'; 
		$("#" + input_style).css("background", 'red');
		qestion.push(1) 
		localStorage.setItem(task_status, 'false')
		fasle_questions_in_answer += question_body;
		localStorage.setItem( 'flase_question_body', fasle_questions_in_answer );
	} 
	$("." + task_test_block + " input").prop("disabled", true);

}

function checkIdentidyTask(name, border_color) { 
	var task_name = document.getElementsByClassName(name);
	var border_color = document.getElementsByClassName(border_color)

	
	for (i = 0; i < task_name.length; i++) {
		if (task_name[i].checked){
			if (!selected_task) {
				last_selected_task_id = i;
				selected_task = task_name[i].value; 
				task_name[i].disabled = true;
				task_name[i].checked = false;

				border_color[i].style = ('border: 2px solid ' + colors[color_id]);
				// border_color[i].style += ('box-shadow: 0 0 5px ' + colors[color_id]);

			} 
			else { 
				task_name[last_selected_task_id].disabled = false;
				task_name[last_selected_task_id].checked = true;
				border_color[last_selected_task_id].style = ('border: 2px solid gray');
				
				last_selected_task_id = i;
				selected_task = task_name[i].value;
				// console.log(selected_task)
				task_name[i].disabled = true;
				task_name[i].checked = false;

				border_color[i].style = ('border: 2px solid ' + colors[color_id]);
				
			}

		}
	selected = true;
		
	}  

}
function checkIdentidyAnswer(name, border_color) {
	if (selected) {
		var task_name = document.getElementsByClassName(name); 
		var border_color = document.getElementsByClassName(border_color)
		for (i = 0; i < task_name.length; i++) {
			if (task_name[i].checked){
				selected_answer = task_name[i].value;
				// console.log(selected_answer)
				task_name[i].disabled = true;
				task_name[i].checked = false;
				border_color[i].style = ('border: 2px solid ' + colors[color_id])
				color_id ++
				if (color_id == 4) {
					color_id = 0;
				}

			} 
		}  
		if (selected_answer == selected_task) {
			console.log(true)  
			identify_question.push(0) 
			selected_task = null;
		} else {
			console.log(false)  
			identify_question.push(1) 
		}
		selected = false;
	} else {
		alert('Сол жақтағы блокты бірінші таңдаңыз')
	}
}

function  checkIdentidyButton(identify_question, result_block, task_id, button, identifyOpen, question_body){
	console.log(identify_question)
	console.log(identify_question.reduce((a, b) => a + b, 0))

	if (identify_question.reduce((a, b) => a + b, 0) == 0) {
		document.getElementById(result_block).innerHTML = 'Дұрыс';
		$("#" + identifyOpen).css("background", '#02a0da'); 
		localStorage.setItem(task_id, 'Дұрыс')
		qestion.push(0) 


	} else {
		document.getElementById(result_block).innerHTML = 'Қате';
		localStorage.setItem(task_id, 'Қате')		
		$("#" + identifyOpen).css("background", 'red'); 
		qestion.push(1) 	
		fasle_questions_in_answer += question_body;
		localStorage.setItem( 'flase_question_body', fasle_questions_in_answer );


	}
	document.getElementById(button).style.display = 'none';
	var identify_question;
	identify_question = []
	console.log(identify_question)
}  

function nextPage() {
	// var button_id = 
}	