function getListStudentIds(getListStudents) {
  for (const obj of getListStudents) {
    if (typeof obj !== 'object' || !Array.isArray(getListStudents)) {
      return [];
    }
  }
  const newArrayById = getListStudents.map((student) => student.id);
  return newArrayById;
}

export default getListStudentIds;
