function getListStudents() {
	const keys =['id', 'firstName', 'location'];
	const values = [1, 'Guillaume', 'San Francisco'];
	const values1 = [2, 'James', 'Columbia'];
	const values2 = [3, 'Serena', 'San Francisco'];
	const obj = {};
	const obj1 = {};
	const obj2 = {};
	keys.forEach((key, index) =>{
		obj[key]= values[index];
		obj1[key]= values1[index];
		obj2[key]= values2[index];
	})
	const array = []
	const objAll = array.push(obj, obj1, obj2);
	// ObjAll return le nombre d'obj
	//Array contient les obj
	console.log(objAll)
	return array;
};

export default getListStudents;
