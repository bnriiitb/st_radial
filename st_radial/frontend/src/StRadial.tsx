import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import Chart from "react-apexcharts"

class StRadial extends StreamlitComponentBase {

  public render = (): ReactNode => {

    const title = this.props.args["title"]
    const value = this.props.args['value']
    const startAngle = this.props.args['start_angle']
    const endAngle = this.props.args['end_angle']
    
    const { theme } = this.props

      const config = {
        options: {
          plotOptions: {
            radialBar: {
              startAngle: startAngle,
              endAngle: endAngle,
              hollow: {
                size: "70%",
                background: "#fff",
              },
              dataLabels: {
                name: {
                  offsetY: -20,
                  color: "#888",
                  fontSize: "0.8rem"
                },
                value: {
                  formatter: function (val: any) {
                    return val;
                  },
                  color: "#111",
                  fontSize: "2.25rem",
                }
              }
            }
          },
          labels: [title],
          stroke: {
            lineCap: 'round' as 'round'
          },
        },
        series: [value],
      }

    if (theme) {
      config.options.plotOptions.radialBar.hollow.background = theme.backgroundColor
      config.options.plotOptions.radialBar.dataLabels.value.color = theme.textColor
      config.options.plotOptions.radialBar.dataLabels.name.color = theme.textColor
    }

    return (
      <div>
          <Chart
            options={config.options}
            series={config.series}
            type="radialBar"
            width="250"
          />
      </div>
    )
  }
}

export default withStreamlitConnection(StRadial)
