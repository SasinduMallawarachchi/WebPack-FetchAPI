    async function addEmployeeRestApi(){
    try{
        const employee = [
            {   
                "id" : "3",
                "firstName" : "Kasun",
                "lastName" : "Mallawarachchi",
                "email" : "sasindu@gmail.com"
            }
        ]
        const response = await fetch("https://j5igw9ry82.execute-api.eu-north-1.amazonaws.com/test/sampleapi",{
                method: 'POST',
                 mode: 'cors',
                body: JSON.stringify(employee),
                headers:{
                'Content-Type': 'application/json',
            }
        })
                const data = await response.json();
                console.log(response.status);
                console.log("POST",data);
    }catch(error){
        console.log(error);
    }
  }

  export default addEmployeeRestApi