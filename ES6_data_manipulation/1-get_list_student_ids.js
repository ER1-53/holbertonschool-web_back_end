function getListStudentIds(getListStudents) {

if (!Array.isArray(getListStudents)) {
	return [];
}
  const newArrayById = getListStudents.map((student) => student.id);
  return newArrayById;
}

export default getListStudentIds;
