function getPackage(){
	var chosenPackage = document.getElementById("package");
	chosenPackage = chosenPackage.value;
	return chosenPackage;
}

function getComponant(){
	var chosenComponant = document.getElementById("componant");
	chosenComponant = chosenComponant.value;
	return chosenComponant;
}

function getIssue(){
	var chosenIssue = document.getElementById("issue");
	chosenIssue = chosenIssue.value;
	return chosenIssue;
}

function getStartDay(){
	var startDay = document.getElementById("sDay");
	startDay = parseInt(startDay.value);
	return startDay;
}

function getStartMonth(){
	var startMonth = document.getElementById("sMonth");
	startMonth = parseInt(startMonth.value);
	return startMonth;
}

function getEndDay(){
	var endDay = document.getElementById("rDay");
	endDay = parseInt(endDay.value);
	return endDay;
}

function getEndMonth(){
	var endMonth = document.getElementById("rMonth");
	endMonth = parseInt(endMonth.value);
	return endMonth;
}

function calcTotal(){
	var startMonth = getStartMonth();
	var endMonth = getEndMonth();
	var startDay = getStartDay();
	var endDay = getEndDay();
	var daysInFirstMonth = getNoOfDays(startMonth);
	var daysInEndMonth = getNoOfDays(endMonth);
	var packagePrice = getNewPackage();
	var chosenIssue = getIssue();
	var adjustment = 0;

	if(startMonth == endMonth){
		adjustment += packagePrice / daysInFirstMonth * ((endDay - startDay) + 1);
	} else {
		while(startMonth != endMonth){
			adjustment += packagePrice / daysInFirstMonth * daysInFirstMonth;
			startMonth ++;
			if(startMonth == 13){
				startMonth = 1;
			}
		}
		adjustment += packagePrice / daysInEndMonth * endDay;
	}

	if(chosenIssue == "intermittent"){
		adjustment = adjustment / 2;
	}

	if(validateFields()){
		alert("Adjustment due: €" + (Math.round(adjustment * 100) / 100));
		return true;
	} else {
		alert("Please complete the remaining fields");
		return false;
	}
}

function getNewPackage(){
	var chosenPackage = getPackage();
	var chosenComponant = getComponant();
	var chosenIssue = getIssue();

	if(chosenPackage == "simply"){
		return 38;
	} else if(chosenPackage == "essentials"){
		if(chosenComponant == "ll"){
			return 35;
		} else if(chosenComponant == "bb"){
			return 10;
		} else {
			return 45;
		}
	} else if(chosenPackage == "ultimate"){
		if(chosenComponant == "ll"){
			return 45;
		} else if(chosenComponant == "bb"){
			return 10;
		} else {
			return 55;
		}
	}
}

function getNoOfDays(month){
	var months = [31,28,31,30,31,30,31,31,30,31,30,31];
	var input = [01,02,03,04,05,06,07,08,09,10,11,12];
	var noOfDays = months[input.indexOf(parseInt(month))];
	return noOfDays;
}

function refreshComponantList(){
	var chosenPackage = getPackage();
	
	if(chosenPackage == "simply"){
		componant.value = "bb";
		componant.disabled = true;
	} else {
		componant.disabled = false;
	}
}

function validateFields(){
	var checkPackage = getPackage();
	var checkComponant = getComponant();
	var checkIssue = getIssue();
	var checkStartDay = getStartDay();
	var checkStartMonth = getStartMonth();
	var checkEndDay = getEndDay();
	var checkEndMonth = getEndMonth();

	if(checkPackage == "--select package--" || checkComponant == "--select componant--" || checkIssue == "--select issue--" || isNaN(checkStartDay) || isNaN(checkStartMonth) || isNaN(checkEndDay) || isNaN(checkEndMonth)){
		return false;
	} else {
		return true;
	}
}