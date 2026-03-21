
class reusable:

    def dropColumns(self, df, columns):
        for column in columns:
            df = df.drop(column)
        return df