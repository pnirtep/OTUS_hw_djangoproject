import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courses_site.settings.settings_local")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import json
from graphene_django.utils.testing import GraphQLTestCase
from . import schema


class CoursesTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_query(self):
        response = self.query(
            '''
            query {
                allCourses{
                    title
                    description
                    price
                }
            }
            ''',
            op_name='allCourses'
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_query_one_course(self):
        response = self.query(
            '''
            query
                course($id: Int!){
                    course(id: $id) {
                    id
                }
                }
            ''',
            op_name='course',
            variables={'id': 10}
        )

        content = json.loads(response.content)
        print(response)
        self.assertResponseNoErrors(response)

    def test_createCourse_mutation(self):
        response = self.query(
            '''
            mutation {
               newCourse(newTitle:"Web-python4", newDescription:"Продвинутый курс по веб-разработке", newPrice:13990){
                result
                course{
                  title
                  description
                }
              }
            }
            ''',
            op_name='newCourse'
        )

        self.assertResponseNoErrors(response)
        self.assertEqual(response.status_code, 200)
