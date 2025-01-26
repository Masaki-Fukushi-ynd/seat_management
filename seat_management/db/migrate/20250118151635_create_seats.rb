class CreateSeats < ActiveRecord::Migration[8.0]
  def change
    create_table :seats do |t|
      t.integer :table_number, null: false
      t.integer :seat_number, null: false 
      t.boolean :is_occupied, default: false, null: false
      t.string :identifier, null: false

      t.timestamps
    end
  end
end
