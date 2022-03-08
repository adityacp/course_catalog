<template>
  <div class="container-fluid">
    <div class="spinner-border" role="status" v-if="isLoading">
      <span class="sr-only">Loading...</span>
    </div>
    <div class="row">
      <div class="col-3">
        <h4><b>Search for Keywords</b></h4>
        <label class="sr-only" for="inlineFormInputGroup">Filter Courses</label>
        <div class="input-group mb-2">
          <div class="input-group-prepend">
            <div class="input-group-text">
              <i class="fa fa-search"></i>
            </div>
          </div>
          <input type="text" class="form-control" id="inlineFormInputGroup" placeholder="Filter Courses" v-model="name">
        </div>
        <br>
        <h4><b>Category</b></h4>
        <div class="form-check" :key="category" v-for="category in categories">
          <input class="form-check-input" type="radio" v-model="selectedCategory" :value="category">
          <label class="form-check-label" for="flexRadioDefault1">
            {{category}}
          </label>
        </div>
      </div>
      <div class="col">
        <div class="row">
          <div class="col-md-5" :key="idx"  v-for="(course, idx) in filteredCourses">
            <div class="card shadow p-3 mb-5 bg-white rounded">
              <div class="card-body">
                <div class="row">
                  <div class="col-2">
                     <div class="badge badge-pill badge-primary">1</div>
                  </div>
                  <div class="col">
                    <div class="title">
                      <h6>{{course.name}}</h6><br>
                    </div>
                    <b>{{course.instructor__first_name}} {{course.instructor__last_name}}</b>
                  </div>
                </div>
                <br>
                <div class="row">
                  <div class="col-2">
                    <i class="fa fa-info-circle" aria-hidden="true"></i>
                  </div>
                  <div class="col"><p align="justify">{{course.description}}</p></div>
                </div>
                <br>
                <div class="row">
                  <div class="col-2">
                    <i class="fa fa-calendar" aria-hidden="true"></i>
                  </div>
                  <div class="col">
                    <p align="justify">
                    <b>{{getCourseStatus(course.start_date, course.end_date)}}</b>
                    <b>{{getFormattedDate(course.start_date)}} - {{getFormattedDate(course.end_date)}}</b>
                    {{course.weeks}} week course, {{course.estimated_workload}}
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <br>
          </div>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>

import CourseService from "../../services/CourseService"

export default {
  name: 'Course',
  data() {
    return {
      categories: [],
      courses: [],
      isLoading: false,
      selectedCategory: "All",
      name: ""
    }
  },
  computed: {
    filteredCourses: function() {
      var vm = this;
      var category = vm.selectedCategory;
      var filter_name = vm.name.toLowerCase()
      if (category === "All" && filter_name === "") {
        return this.courses
      }
      else {
        if (category != "All") {
          return this.courses.filter(course => {
            return course.category__name === category
          })
        }
        else if(filter_name) {
          return this.courses.filter(course => {
            return course.name.toLowerCase().includes(filter_name)
          })
        } else {
          return this.courses
        }
      }
    },
  },
  mounted() {
    this.getAllCategories();
    this.getAllCourses();
  },
  methods: {
    getAllCourses() {
      this.isLoading = true;
      CourseService.getCourses().then(response => {
        this.courses = response.data.data;
        this.no_courses = this.courses.length;
      })
      .catch(e => {
        console.log(e.message)
      })
      .finally(() => {
        this.isLoading = false;
      });
    },
    getAllCategories() {
      this.isLoading = true;
      CourseService.getCategories().then(response => {
        this.categories = response.data.data;
        this.categories.push("All");
        this.categories.sort();
      })
      .catch(e => {
        console.log(e.message)
      })
      .finally(() => {
        this.isLoading = false;
      });
    },
    getFormattedDate(date) {
      var formatted_date = new Date(date);
      return formatted_date.toLocaleString('default', { month: 'long' }) + " " + formatted_date.getDate();
    },
    getCourseStatus(start_date, end_date) {
      var status;
      var startdate = new Date(start_date);
      var enddate = new Date(end_date);
      var today = new Date();
      if (today < startdate) {
        status = "Pre-registration"
      }
      else if(startdate < today < enddate) {
        status = "Ongoing"
      }
      else {
        status = "Completed"
      }
      return status;
    }
  }
}
</script>
<style scoped>
  .form-check {
    display: flex;
    align-items: flex-start;
  }
  h4 {
    display: flex;
    align-items: flex-start;
    font-size: 0.75rem;
  }
  .card {
    height: 28rem;
  }
  p {
    font-size: 0.75rem;
  }
  .title {
    display: flex;
    align-items: flex-start;
  }
  b {
    display: flex;
    align-items: flex-start;
    font-size: 12px;
  }
  .badge {
     border-radius: 0;
     font-size: 12px;
     line-height: 1;
     padding: .375rem .5625rem;
     font-weight: normal
 }

 .badge-primary {
     color: #ADD8E6;
     border: 1px solid #ADD8E6
 }

 .badge.badge-pill {
     border-radius: 10rem
 }
</style>