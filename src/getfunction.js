//GET
const BASE_URL="https://j5igw9ry82.execute-api.eu-north-1.amazonaws.com/test";

    async function getFunction(id){
        const endpoint=`${BASE_URL}/sampleapi?id=${id}`;
        try{
            let response=await fetch(endpoint,{
                method: 'GET',
                mode: 'cors',
                headers:{
                    'Content-Type': 'application/json',
                    'x-api-key' : 'API-KEY'
                }
            });
            let data = await response.text();
            console.log(data);
        }catch(error){
            console.log(error);
        }
    }

 export default getFunction