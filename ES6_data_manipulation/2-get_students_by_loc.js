function getStudentsByLocation(getListStudents, city) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  const newArrayByCity = getListStudents.filter((student) => student.location === city);
  return newArrayByCity;
}

export default getStudentsByLocation;
