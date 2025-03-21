def main(input_file_name = "src/testcase.txt", output_file_name = "src/output.txt"):
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")

    data = {}

    for i in input_file:
        city, temp = i.strip().split(';')
        # print(city)
        # print(temp)
        temp = float(temp)
        
        if city not in data:
            data[city] = []
        data[city].append(temp)

    #print(OK)
    # print(data.keys())
    
    city_names = sorted(data.keys())
    # print(city_names)
    # print(data)
    
    x = 0

    for i in (city_names):
        temp = data[i]
        # print(temp)
        min_temp = min(temp)
        # print(min_temp)
        max_temp = max(temp)
        sum = 0
        for j in temp:
            sum += float(j)
        mean_temp = sum / len(temp) 
        
        res = f"{city_names[x]}={min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}\n"
        x += 1
        # print(res)
        output_file.write(res)
        
    output_file.close()
    input_file.close()

if __name__ == "__main__":
    main()