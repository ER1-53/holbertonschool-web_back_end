export default (departmentName, employees) => {
  return {[departmentName]: [...employees]};
};
