import http from "../http-common";

class CourseService {
  getCourses() {
    return http.get("/courses");
  }
  getCategories() {
    return http.get("/categories");
  }
}

export default new CourseService();
