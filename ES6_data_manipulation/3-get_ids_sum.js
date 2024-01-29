function getStudentIdsSum(getListStudents) {
	
  const sumOfId = getListStudents.reduce((total, student) => total + student.id, 0);
  return sumOfId;
}

export default getStudentIdsSum;
