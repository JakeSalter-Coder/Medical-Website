function submitButton(){

    let user_first_name = document.getElementById("first_name").value;
    let user_last_name = document.getElementById("last_name").value;
    let user_age = document.getElementById("age").value
    let user_gender;
    if(document.getElementById("male").checked){
        user_gender = "male";
    } else if(document.getElementById("female").checked){
        user_gender = "female";
    } else{
        user_gender = "other";
    }
    let user_height = document.getElementById("height").value;
    let user_weight = document.getElementById("weight").value;
    let user_race = document.getElementById("race").value;

    let errorMessage = document.getElementById("error_message");

    if(user_first_name && user_last_name && user_age && user_gender && user_height && user_weight && user_race) {
        $.ajax({
            url: '/submit',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                first_name: user_first_name,
                last_name: user_last_name,
                age: user_age,
                gender: user_gender,
                height: user_height,
                weight: user_weight,
                race: user_race
            }),
            success: function(response){
                alert('Data submit successfully: ' + JSON.stringify(response));
            },
            error: function(error){
                alert('Error submitting data: ' + error);
            }
        });
    }
}