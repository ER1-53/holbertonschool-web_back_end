function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const filterByCity = getListStudents.filter((student) => student.location === city);
  const updateStudent = filterByCity.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

    if (matchingGrade) {
      return { ...student, grade: matchingGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });
  return updateStudent;
}

export default updateStudentGradeByCity;
