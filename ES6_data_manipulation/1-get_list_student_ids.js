function getListStudentIds(getListStudents) {
  if (Array.isArray(getListStudents)) {
    const newArrayById = getListStudents.map((student) => student.id);
    return newArrayById;
  }
  return [];
}

export default getListStudentIds;
