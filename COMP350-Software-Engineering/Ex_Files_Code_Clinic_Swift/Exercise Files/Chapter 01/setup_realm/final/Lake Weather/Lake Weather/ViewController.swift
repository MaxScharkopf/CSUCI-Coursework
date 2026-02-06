//
//  ViewController.swift
//  Lake Weather
//
//  Created by Todd Perkins on 4/16/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit
import Foundation
import RealmSwift


class DayData: Object {
    let date = RealmOptional<Int>()
    @objc dynamic var time: String? = nil
    let AirTemp = RealmOptional<Double>()
    let BarometricPressure = RealmOptional<Double>()
    let DewPoint = RealmOptional<Double>()
    let RelativeHunidity = RealmOptional<Double>()
    let WindDir = RealmOptional<Double>()
    let WindGust = RealmOptional<Int>()
    let WindSpeed = RealmOptional<Double>()
}

class ViewController: UIViewController {
    @IBOutlet weak var activityView: UIView!
    @IBOutlet weak var medianSpeedLabel: UILabel!
    @IBOutlet weak var meanSpeedLabel: UILabel!
    @IBOutlet weak var meanPressureLabel: UILabel!
    @IBOutlet weak var medianPressureLabel: UILabel!
    @IBOutlet weak var meanTempLabel: UILabel!
    @IBOutlet weak var medianTempLabel: UILabel!
    @IBOutlet weak var startPicker: UIDatePicker!
    @IBOutlet weak var endPicker: UIDatePicker!
    var realm:Realm!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        activityView.isHidden = true
        loadRealm()
    }
    
    func loadRealm() {
        do {
            var config = Realm.Configuration()
            config.objectTypes = [DayData.self]
            realm = try Realm(configuration: config)
            
            // Only import CSV if DB is empty
            if realm.objects(DayData.self).isEmpty {
                importCSV()
            }
            print("Total records in Realm: \(realm.objects(DayData.self).count)")
            updateDays()
        } catch {
            print(error)
        }
    }

    func importCSV() {
        guard let path = Bundle.main.path(forResource: "DayData", ofType: "csv"),
              let content = try? String(contentsOfFile: path) else { return }
        
        let rows = content.components(separatedBy: "\n") // skip header
        try? realm.write {
            for row in rows {
                let cols = row.components(separatedBy: ",")
                guard cols.count >= 9 else { continue }
                let day = DayData()
                day.date.value = Int(cols[0].trimmingCharacters(in: .whitespaces))
                day.time = cols[1].trimmingCharacters(in: .whitespaces)
                day.AirTemp.value = Double(cols[2].trimmingCharacters(in: .whitespaces))
                day.BarometricPressure.value = Double(cols[3].trimmingCharacters(in: .whitespaces))
                day.DewPoint.value = Double(cols[4].trimmingCharacters(in: .whitespaces))
                day.RelativeHunidity.value = Double(cols[5].trimmingCharacters(in: .whitespaces))
                day.WindDir.value = Double(cols[6].trimmingCharacters(in: .whitespaces))
                day.WindGust.value = Int(Double(cols[7].trimmingCharacters(in: .whitespaces)) ?? 0)
                day.WindSpeed.value = Double(cols[8].trimmingCharacters(in: .whitespaces))
                realm.add(day)
            }
        }
    }
    
    @IBAction func didPressUpdate(_ sender: Any) {
        activityView.isHidden = false
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.01) {
            self.updateDays()
            self.activityView.isHidden = true
        }
        
    }
    
    func updateDays() {
        
        let d1 = startPicker.date
        let d2 = endPicker.date
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyyMMdd"
        let startDate = Int(formatter.string(from: d1))!
        let endDate = Int(formatter.string(from: d2))!
        
        let data:Results<DayData> = realm.objects(DayData.self).filter("date >= \(startDate) AND date <= \(endDate)")
        
        if data.count < 2{
            showMessage(message: "Insufficient data. Please change start and/or end date.")
            return
        }
        
        let dataForStartDate = (data[0].date.value! == startDate)
        let dataForEndDate = (data.last!.date.value! == endDate)
        if !dataForStartDate{
            showMessage(message: "No data for start date.")
        }
        if !dataForEndDate{
            showMessage(message: "No data for end date.")
        }
        findAverages(data)
    }
    
    func findAverages(_ data:Results<DayData>) {
        var temps:[Double] = []
        var speeds:[Double] = []
        var pressures:[Double] = []
        for day:DayData in data{
            if let temp = day.AirTemp.value { temps.append(temp) }
            if let speed = day.WindSpeed.value { speeds.append(speed) }
            if let pressure = day.BarometricPressure.value { pressures.append(pressure) }
        }
        medianTempLabel.text = "Median Temperature: \(findMedian(a: temps))"
        meanTempLabel.text = "Mean Temperature: \(findMean(a: temps))"
        medianPressureLabel.text = "Median Pressure: \(findMedian(a: pressures))"
        meanPressureLabel.text = "Mean Pressure: \(findMean(a: pressures))"
        medianSpeedLabel.text = "Median Speed: \(findMedian(a: speeds))"
        meanSpeedLabel.text = "Mean Speed: \(findMean(a: speeds))"
    }
    
    func showMessage(message:String) {
        let alert = UIAlertController(title: "Missing Data", message: message, preferredStyle: .alert)
        let action = UIAlertAction(title: "Ok", style: .default, handler: nil)
        alert.addAction(action)
        self.present(alert, animated: true, completion: nil)
    }
    
    func findMedian(a:[Double]) -> Double {
        guard !a.isEmpty else { return 0.0 }
        let aSorted = a.sorted()
        if aSorted.count % 2 == 0 {
            let middleIndex = aSorted.count / 2 - 1
            return findMean(a:[aSorted[middleIndex],aSorted[middleIndex+1]])
        }
        let middleIndex = Int(floor(Float(aSorted.count)/2.0))
        return aSorted[middleIndex]
    }

    func findMean(a:[Double]) -> Double {
        guard !a.isEmpty else { return 0.0 }
        var total:Double = 0
        for num in a{
            total += num
        }
        return total/Double(a.count)
    }
    
    
    @IBAction func startDateDidChange(_ sender: UIDatePicker) {
        // make sure end date is after start date
        if startPicker.date >= endPicker.date {
            //print("start date is after end date")
            endPicker.date = startPicker.date
        }
    }
    @IBAction func endDateDidChange(_ sender: UIDatePicker) {
        // make sure start date is before end date
        if startPicker.date >= endPicker.date {
            //print("start date is after end date")
            startPicker.date = endPicker.date
        }
    }
    
    override var prefersStatusBarHidden: Bool {
        return true
    }
    
    
}



