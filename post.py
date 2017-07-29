def post(self):
        args = self.reqparse.parse_args()
        return jsonify({'courses': [{'title': 'Python Basics'}]})
