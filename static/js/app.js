
d3.json('/query').then(data => {

    // console.log('hi')
    // console.log(data);

        // Handling click for button1
        var ul = d3.select(".Id_info").append("ul");
        var button1 = d3.select(".button1")

        button1.on("click", function() {  
        ul.html("");


            // finding a random number between 0 and 29 for every click
            number = Math.floor((Math.random() * 29) + 1);
            random_pick = Math.round(Math.random());

            console.log(`random number: ${random_pick}`);
            console.log(`number: ${number}`);

            // extracting data when number = id 
            info = data.filter( element => element.id == number)
            // console.log(info);

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


            if (wash_hands == 0){
                wash_hands = 'NO'
            }
            else{
                wash_hands = 'YES'
            }

            if (touch_face == 0){
                touch_face = 'NO'
            }
            else{
                touch_face = 'YES'
            }

            if (wear_mask == 0){
                wear_mask = 'NO'
            }
            else{
                wear_mask = 'YES'
            }

            if (large_gathering == 0){
                large_gathering = 'NO'
            }
            else{
                large_gathering = 'YES'
            }

            if (truth == 0){
                truth = 'NO'
            }
            else{
                truth = 'YES'
            }

            if (prediction == 0){
                prediction = 'NO'
            }
            else{
                prediction = 'YES'
            }

            details1 = {}
            details1['My Id '] = res_id[0]
            details1['I am a '] = sex[0]
            details1['My Age '] = age[0]
            details1['I am '] = marital_status[0]
            details1['My Income '] = income[0]
            details1['Do I like to wash hands '] = wash_hands
            details1['Do I like to touch face '] = touch_face

            details2 = {}
            details2['My Id '] = res_id[0]
            details2['I am a '] = sex[0]
            details2['My Age '] = age[0]
            details2['I am '] = marital_status[0]
            details2['My education '] = education[0]
            details2['Do I like to wear face mask '] = wear_mask
            details2['Do I like to large gathering '] = large_gathering
            

        //    console.log(details1)

            // Creating the list elements for the info
            if (random_pick == 0) {
                Object.entries(details1).forEach(([key,value]) =>{
            var li = ul.append("li").text(`${key}:${value}`);
            
            });
            }
            else {
                Object.entries(details2).forEach(([key,value]) =>{
                    var li = ul.append("li").text(`${key}:${value}`);
                });
            }
            d3.selectAll("li").style("list-style", "none");
          
                
        });
    

        var button_grp = d3.selectAll(".btn-group")
        // console.log(button_grp);
        button_grp.on("click", function() {  


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
