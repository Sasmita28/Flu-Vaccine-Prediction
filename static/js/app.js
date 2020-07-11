

d3.json('/query').then(data => {

  
    //selecting the 'Id_info" element from html to append 'ul'
    var ul = d3.select(".Id_info").append("ul");

    // selecting the button1(click to know about me button)
    var button1 = d3.select(".button1")


    // Handling click for button1
    button1.on("click", function() {  

        // emptying the page for every click
        ul.html("");


        // finding a random number between 0 and 29 for every click
        number = Math.floor((Math.random() * 29) + 1);

        // finding random number 0 or 1 for random pick of our paragraph
        random_pick = Math.round(Math.random());

        console.log(`random number for paragraph: ${random_pick}`);
        console.log(`number for id: ${number}`);

        // extracting data when number = id 
        info = data.filter( element => element.id == number)
        // console.log(info);

        // extracting data from info to our variables
        res_id = info.map(row=> row.respondent_id);
        sex = info.map(row=> row.sex);
        age = info.map(row=> row.age_group);
        marital_status = info.map(row=> row.marital_status);
        income = info.map(row=> row.income_poverty);
        education = info.map(row=> row.education)
        wash_hands = info.map(row=> row.behavioral_wash_hands);
        touch_face = info.map(row=> row.behavioral_touch_face);
        wear_mask = info.map(row=> row.behavioral_face_mask);
        large_gathering = info.map(row=> row.behavioral_large_gatherings)
        truth = info.map(row=> row.h1n1_vaccine);
        prediction = info.map(row=> row.Prediction);
  
        // initializing the binary_cols dictionary to convert 0 and 1 to 'NO' and 'YES' respectively
        binary_cols = {}

        // assigning keys and values to binary_cols
        binary_cols= {'wash_hands':wash_hands,'touch_face':touch_face,'wear_mask':wear_mask,'large_gathering':large_gathering,'truth':truth,'prediction':prediction}
        
        // converting 0 to 'NO' and 1 to 'YES'
        Object.keys(binary_cols).forEach(function(key){
            if (binary_cols[key] == 1) {
                binary_cols[key] = 'YES'
            }
            else {
                binary_cols[key] = 'NO'
            }

        })
        // console.log(binary_cols);


        // creating details1 and details2 dictionaries for our paragraphs
        details1 = {}
        details1['My Id'] = res_id[0]
        details1['Sex'] = sex[0]
        details1['My Age'] = age[0]
        details1['Marital Status'] = marital_status[0]
        details1['My Income'] = income[0]
        details1['I wash my hands often'] =binary_cols['wash_hands']
        details1['I touch my face often'] = binary_cols['touch_face']

        details2 = {}
        details2['My Id'] = res_id[0]
        details2['Sex'] = sex[0]
        details2['My Age'] = age[0]
        details2['Marital Status'] = marital_status[0]
        details2['My education'] = education[0]
        details2['Do I regularly wear a face mask'] = binary_cols['wear_mask']
        details2['Do I like large gatherings'] = binary_cols['large_gathering']



        
    //    console.log(details1)

        // Creating the list elements in html using details1 dictionary
        if (random_pick == 0) {
            Object.entries(details1).forEach(([key,value]) =>{
                var li = ul.append("li").text(`${key} : ${value}`);
        
        
            });
        }
        else {
            Object.entries(details2).forEach(([key,value]) =>{
                var li = ul.append("li").text(`${key} : ${value}`);
                
            });
        }
        d3.selectAll("li").style("list-style", "none");
      
            
    });

    // handling the 'YES' and 'NO' buttons
    var button_grp = d3.selectAll(".btn-group")
    // console.log(button_grp);
    button_grp.on("click", function() {  

        var truth = binary_cols['truth']
        var prediction = binary_cols['prediction']

        var guess = d3.event.target.value

        if (guess == truth && truth != prediction) {

            var test = 'You beat the Model'

        }
        else if (guess != truth && truth == prediction) {

            var test = 'The Model beat you'

        }
        else if (guess != truth && truth != prediction) {

            var test = 'You both are wrong'

        }
        else {
            var test = 'You both are correct'
        }

            if (guess == 'YES') {
                your_prediction = 'would'
            }
            else{
                your_prediction = 'would not'
            }
            if (prediction == 'YES') {
                model_prediction = 'would'
            }
            else{
               model_prediction = 'would not'
            }

            if (truth == 'YES') {
                truth_response= 'did'
            }
            else{
                truth_response = 'did not'
            }


            var results  = `${test}. You guessed that they ${your_prediction} get a vaccine. The model predicted that they ${model_prediction} get a vaccine. In truth, they ${truth_response} get a vaccine.`
            


            d3.select("#final_answer").html(results);
            
            


    });


});

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("yesNobuttons");

//Get the card
var cardElement = document.getElementById("cardbody");

//Get the button that clears the card
var btn2 = document.getElementById("tryAgain");


// When the user clicks on the yes.no buttons, open the results modal popup
yesNobuttons.onclick = function() {
modal.style.display = "block";
}

//When the "Try Again" button is clicked, the popup disappears and the survey card clears
tryAgain.onclick = function() {
modal.style.display = "none";
cardbody.style.display = "none";


}

//"click to learn about me" button displays next survey data after page load, after starting over on page.
button1.onclick = function() {
cardbody.style.display = "block";
}
