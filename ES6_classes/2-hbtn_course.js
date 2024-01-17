export default class HolbertonCourse {
  constructor (name, length, students) {
    this._name = name,
    this._length = length,
    this._students = students
  };


  get name() {
    return `${this._name}`;
  }
  get length() {
    return `${this._length}`;
  }
  get students() {
    return `${this._students}`;
  }

  set name(value) {
    this._name = value;
  }
  set length(value) {
    this._length = value;
  }
  set students(value) {
    this._students = value;
  }
}
