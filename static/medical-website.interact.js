function submitButton(){

    let user_name = document.getElementById("name").value;
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

    if(user_name && user_age && user_gender && user_height && user_weight && user_race){
        alert("Success!");
        $.post('/',
            {
                name: user_name,
                age: user_age,
                gender: user_gender,
                height: user_height,
                weight: user_weight,
                race: user_race
            },
        );
    } else{
        alert("Incorrect input!");
    }
}